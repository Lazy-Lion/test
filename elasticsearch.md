# 思维导图


![img](E:\GitRepository\test\image\v2-5b3f5e22445109e74e3e67fa3f4556a5_720w.jpg)

![img](E:\GitRepository\test\image\v2-740d6b993e94def9fd84547fe4ef098a_720w.jpg)

![img](E:\GitRepository\test\image\v2-7bf3269cbc937cd64d0a215275afc6f2_720w.jpg)

![img](E:\GitRepository\test\image\v2-bb2d3723ea06097bdca2eecfb2d0e91b_720w.jpg)

![img](E:\GitRepository\test\image\v2-03b12f7b41bbfb450dcf19334c5af50c_720w.jpg)

![img](E:\GitRepository\test\image\v2-69ce1243e44a0970718cb070ef7f3ab8_720w.jpg)



**基于 Elasticsearch 7.10**

# 1  概念

**Cluster, node, index, shard, mapping, type, document, field.**

**Elasticsearch** is the **distributed** search and analytics engine at the heart of the Elastic Stack. **Logstash** and Beats facilitate collecting, aggregating, and enriching your data and storing it in Elasticsearch. **Kibana** enables you to interactively explore, visualize, and share insights into your data and manage and monitor the stack. Elasticsearch is where the indexing, search, and analysis magic happens.

Elasticsearch is a distributed document store. **Elasticsearch stores complex data structures that have been serialized as JSON documents.**

Elasticsearch provides **near real-time** (within one second) search and analytics for all types of data. Elasticsearch uses a data structure called an **inverted index** that supports very fast full-text searches. An inverted index lists every unique word that appears in any document and identifies all of the documents each word occurs in.

An **index** can be thought of as an optimized collection of **document**s and each document is a collection of **field**s, which are the key-value pairs that contain your data.  By default, Elasticsearch indexes all data in every field and each indexed field has a dedicated, optimized data structure.

Under the covers, an Elasticsearch index is really just a logical grouping of one or more physical **shard**s, where each shard is actually a self-contained index. By distributing the documents in an index across multiple shards, and distributing those shards across multiple **node**s, Elasticsearch can ensure redundancy, which both protects against hardware failures and increases query capacity as nodes are added to a **cluster**. As the cluster grows (or shrinks), Elasticsearch automatically migrates shards to rebalance the cluster.

There are two types of shards: **primaries and replicas**. Each document in an index belongs to one primary shard. A replica shard is a copy of a primary shard. Replicas provide redundant copies of your data to protect against hardware failure and increase capacity to serve read requests like searching or retrieving a document.

The number of primary shards in an index is fixed at the time that an index is created, but the number of replica shards can be changed at any time, without interrupting indexing or query operations.

There are a number of performance considerations and trade offs with respect to shard size and the number of primary shards configured for an index.

- Aim to keep the average shard size between a few GB and a few tens of GB. For use cases with time-based data, it is common to see shards in the 20GB to 40GB range.
- Avoid the gazillion shards problem. The number of shards a node can hold is proportional to the available heap space. As a general rule, the number of shards per GB of heap space should be less than 20.

**Mapping** is the process of defining how a document, and the fields it contains, are stored and indexed.

A mapping definition has:

- Metadata fields
  Metadata fields are used to customize how a document’s associated metadata is treated. Examples of metadata fields include the document’s `_index`, `_id`, and `_source` fields.
- Fields
  A mapping contains a list of fields or properties pertinent to the document. Each field has its own data type.
- Before 7.0.0, the *mappings* definition used to include a **type** name. 

![img](E:\GitRepository\test\image\v2-60e13437fac9b43c13fc2f33a8de817b_720w.jpg)

# 2 节点和分片

### 2.1 节点角色分类

##### 2.1.1 Master Node

默认`node.master:true`，称为`Master-eligible Node`，表示当前有资格成为`Master Node`。`Master Node`只能有一个，负责维护集群状态（所有节点的信息，所有索引Mapping信息，配置信息，分片路由）。

##### 2.1.2 Data Node

默认`node.data:true`，存储数据的节点。

##### 2.1.3 Coordinating Node

用于协调客户端的请求，将接收到的请求分发给合适的节点，并把结果汇集。

##### 2.1.4 Ingest Node



### 2.2 分片

##### 2.2.1 主分片 (primary shard)

主分片在创建索引时确定，后续不能修改。

##### 2.2.2 副本分片 (replica shard)

副本分片在创建索引后可以修改。副本分片可以负载读请求，不能负载写请求。

# 2  数据类型

本节中请求示例基于 `elasticsearch 7.10`，`7.0`之前的版本`mapping`的定义需要包含`type`的名称。

```json
// version 6.8
PUT my_index
{
  "mappings": {
    "_doc": {
      "properties": {
        "tags": {
          "type":  "keyword"
        }
      }
    }
  }
}

// version 7.9
PUT my-index-000001
{
  "mappings": {
    "properties": {
      "tags": {
        "type":  "keyword"
      }
    }
  }
}
```



### String

##### text - 分词

```json
PUT my-index-000001
{
  "mappings": {
    "properties": {
      "full_name": {
        "type":  "text"
      }
    }
  }
}
```

| Parameters for text field | info |
| ------------------------- | ---- |
| analyzer                         | The `analyzer` which should be used for the `text` field, both at index-time and at search-time (unless overridden by the `search_analyzer`). Defaults to the default index analyzer, or the `standard analyzer`. |
| fields | Multi-fields  |
| index | Should the field be searchable? Accepts `true` (default) or `false`. |
| store | Whether the field value should be stored and retrievable separately from the `_source` field. Accepts `true` or `false` (default). |
| search_analyzer |The analyzer that should be used at **search time** on the text field. Defaults to the analyzer setting.|
https://www.elastic.co/guide/en/elasticsearch/reference/current/text.html#fielddata-mapping-param

##### keyword - 不分词

```json
PUT my-index-000001
{
  "mappings": {
    "properties": {
      "tags": {
        "type":  "keyword"
      }
    }
  }
}
```

Not all numeric data should be mapped as a `numeric` field data type. Elasticsearch optimizes numeric fields, such as integer or long, for `range` queries. However, **`keyword` fields are better for `term` and other `term-level` queries.**

##### constant keyword

Constant keyword is a specialization of the `keyword` field for the case that all documents in the index have the same value.

```json
PUT logs-debug
{
  "mappings": {
    "properties": {
      "@timestamp": {
        "type": "date"
      },
      "message": {
        "type": "text"
      },
      "level": {
        "type": "constant_keyword", 
        "value": "debug"
      }
    }
  }
}
```

In case no `value` is provided in the mappings, the field will automatically configure itself based on the value contained in the first indexed document. 

##### wildcard 

```json
PUT my-index-000001
{
  "mappings": {
    "properties": {
      "my_wildcard": {
        "type": "wildcard"
      }
    }
  }
}

PUT my-index-000001/_doc/1
{
  "my_wildcard" : "This string can be quite lengthy"
}

GET my-index-000001/_search
{
  "query": {
    "wildcard": {
      "my_wildcard": {
        "value": "*quite*lengthy"
      }
    }
  }
}
```



### date

```json
PUT my-index-000001
{
  "mappings": {
    "properties": {
      "date": {
        "type": "date" // use the default `format`
      }
    }
  }
}

PUT my-index-000001/_doc/1
{ "date": "2015-01-01" } // This document uses a plain date.

PUT my-index-000001/_doc/2
{ "date": "2015-01-01T12:10:30Z" } // This document includes a time.

PUT my-index-000001/_doc/3
{ "date": 1420070400001 } // This document uses milliseconds-since-the-epoch.

GET my-index-000001/_search
{
  "sort": { "date": "asc"} // Note that the `sort` values that are returned are all in milliseconds-since-the-epoch.
}
```

```json
PUT my-index-000001
{
  "mappings": {
    "properties": {
      "date": {
        "type":   "date",
        "format": "yyyy-MM-dd HH:mm:ss||yyyy-MM-dd||epoch_millis" // Multiple formats can be specified by separating them with `||` as a separator. 一旦我们规定了格式，如果新增数据不符合这个格式，ES将会报mapper_parsing_exception异常。
      }
    }
  }
}
```

### Arrays

In Elasticsearch, there is no dedicated `array` data type. Any field can contain zero or more values by default, however, all values in the array must be of the same data type. 

When adding a field dynamically, the first value in the array determines the field `type`.

An array may contain `null` values, which are either replaced by the configured `null_value` or skipped entirely. An empty array `[]` is treated as a missing field — a field with no values.

**Arrays of objects do not work as you would expect: you cannot query each object independently of the other objects in the array. If you need to be able to do this then you should use the *nested* data type instead of the object data type.**

```
an array of strings: [ "one", "two" ]
an array of integers: [ 1, 2 ]
an array of arrays: [ 1, [ 2, 3 ]] which is the equivalent of [ 1, 2, 3 ]
an array of objects: [ { "name": "Mary", "age": 12 }, { "name": "John", "age": 10 }]
```

```json
PUT my-index-000001/_doc/1
{
  "message": "some arrays in this document...",
  "tags":  [ "elasticsearch", "wow" ], // The tags field is dynamically added as a `string ` field.
  "lists": [ // The lists field is dynamically added as an `object` field.
    {
      "name": "prog_list",
      "description": "programming list"
    },
    {
      "name": "cool_list",
      "description": "cool stuff list"
    }
  ]
}

PUT my-index-000001/_doc/2 // This document contains no arrays, but can be indexed into the same fields.
{
  "message": "no arrays in this document...",
  "tags":  "elasticsearch",
  "lists": {
    "name": "prog_list",
    "description": "programming list"
  }
}

GET my-index-000001/_search
{
  "query": {
    "match": {
      "tags": "elasticsearch"  // The query looks for elasticsearch in the tags field, and matches both documents.
    }
  }
}
```



### object

```json
PUT my-index-000001/_doc/1
{ // The outer document is also a JSON object.
  "region": "US",
  "manager": { // It contains an inner `object` called `manager`.
    "age":     30,
    "name": {  // Which in turn contains an inner `object` called `name`.
      "first": "John",
      "last":  "Smith"
    }
  }
}
```

Internally, this document is indexed as a simple, flat list of key-value pairs, something like this:

```json
{
  "region":             "US",
  "manager.age":        30,
  "manager.name.first": "John",
  "manager.name.last":  "Smith"
}
```

### nested

The `nested` type is a specialised version of the `object` data type that allows arrays of objects to be indexed in a way that they can be queried independently of each other.

When ingesting key-value pairs with a large, arbitrary set of keys, you might consider modeling each key-value pair as its own nested document with `key` and `value` fields. Instead, consider using the `flattened` data type, which maps an entire object as a single field and allows for simple searches over its contents. Nested documents and queries are typically expensive, so using the `flattened` data type for this use case is a better option.

```json
PUT my-index-000001/_doc/1
{
  "group" : "fans",
  "user" : [ 
    {
      "first" : "John",
      "last" :  "Smith"
    },
    {
      "first" : "Alice",
      "last" :  "White"
    }
  ]
}
```

The previous document would be transformed internally into a document that looks more like this:

```json
{
  "group" :        "fans",
  "user.first" : [ "alice", "john" ],
  "user.last" :  [ "smith", "white" ]
}
```

This document would incorrectly match a query for `alice AND smith`.

```json
PUT my-index-000001
{
  "mappings": {
    "properties": {
      "user": {
        "type": "nested" // The user field is mapped as type `nested` instead of type `object`.
      }
    }
  }
}

PUT my-index-000001/_doc/1
{
  "group" : "fans",
  "user" : [
    {
      "first" : "John",
      "last" :  "Smith"
    },
    {
      "first" : "Alice",
      "last" :  "White"
    }
  ]
}

GET my-index-000001/_search
{
  "query": {
    "nested": {
      "path": "user",
      "query": {
        "bool": {
          "must": [ // This query doesn’t match because Alice and Smith are not in the same nested object.
            { "match": { "user.first": "Alice" }},
            { "match": { "user.last":  "Smith" }} 
          ]
        }
      }
    }
  }
}

GET my-index-000001/_search
{
  "query": {
    "nested": {
      "path": "user",
      "query": {
        "bool": {
          "must": [ // This query matches because Alice and White are in the same nested object.
            { "match": { "user.first": "Alice" }},
            { "match": { "user.last":  "White" }} 
          ]
        }
      },
      "inner_hits": {  // inner_hits allow us to highlight the matching nested documents.
        "highlight": {
          "fields": {
            "user.first": {}
          }
        }
      }
    }
  }
}
```

### flattened

```json
PUT bug_reports
{
  "mappings": {
    "properties": {
      "title": {
        "type": "text"
      },
      "labels": {
        "type": "flattened"
      }
    }
  }
}

POST bug_reports/_doc/1 
{ 
  "title": "Results are not sorted correctly.",
  "labels": { // During indexing, tokens are created for each leaf value in the JSON object. The values are indexed as string keywords, without analysis or special handling for numbers or dates.
    "priority": "urgent",
    "release": ["v1.2.5", "v1.3.0"],
    "timestamp": {
      "created": 1541458026,
      "closed": 1541457010
    }
  }
}

POST bug_reports/_search
{
  "query": { // Querying the top-level flattened field searches all leaf values in the object
    "term": {"labels": "urgent"}
  }
}

POST bug_reports/_search
{
  "query": { // To query on a specific key in the flattened object
    "term": {"labels.release": "v1.3.0"}
  }
}
```

### geo_point

Fields of type `geo_point` accept latitude-longitude pairs.

```json
PUT my-index-000001
{
  "mappings": {
    "properties": {
      "location": {
        "type": "geo_point"
      }
    }
  }
}

PUT my-index-000001/_doc/1
{
  "text": "Geo-point as an object",
  "location": { // 1. Geo-point expressed as an object, with lat and lon keys.
    "lat": 41.12,
    "lon": -71.34
  }
}

PUT my-index-000001/_doc/2
{
  "text": "Geo-point as a string",
  "location": "41.12,-71.34" // 2.Geo-point expressed as a string with the format: "lat,lon".
}

PUT my-index-000001/_doc/3
{
  "text": "Geo-point as a geohash",
  "location": "drm3btev3e86" // 3.Geo-point expressed as a geohash.
}

PUT my-index-000001/_doc/4
{
  "text": "Geo-point as an array",
  "location": [ -71.34, 41.12 ] // 4. Geo-point expressed as an array with the format: [ lon, lat], 注意经纬度顺序
}

PUT my-index-000001/_doc/5
{
  "text": "Geo-point as a WKT POINT primitive",
  "location" : "POINT (-71.34 41.12)" // 5.Geo-point expressed as a `Well-Known` Text POINT with the format: "POINT(lon lat)"，注意经纬度顺序
}

GET my-index-000001/_search
{  
  "query": {
    "geo_bounding_box": {  // 6.A geo-bounding box query which finds all geo-points that fall inside the box.
      "location": {
        "top_left": {
          "lat": 42,
          "lon": -72
        },
        "bottom_right": {
          "lat": 40,
          "lon": -74
        }
      }
    }
  }
}
```

```json
PUT /my_locations
{
  "mappings": {
    "properties": {
      "pin": {
        "properties": {
          "location": {
            "type": "geo_point"
          }
        }
      }
    }
  }
}

PUT /my_locations/_doc/1
{
  "pin": {
    "location": {
      "lat": 40.12,
      "lon": -71.34
    }
  }
}

GET /my_locations/_search
{
  "query": {
    "bool": {
      "must": {
        "match_all": {}
      },
      "filter": {
        "geo_distance": {  // 距离查询：距离[-70,40] 200km
          "distance": "200km",
          "pin.location": {
            "lat": 40,
            "lon": -70
          }
        }
      }
    }
  }
```

### histogram

```json
PUT my-index-000001
{
  "mappings" : {
    "properties" : {
      "my_histogram" : {
        "type" : "histogram"
      },
      "my_text" : {
        "type" : "keyword"
      }
    }
  }
}

PUT my-index-000001/_doc/1
{
  "my_text" : "histogram_1",
  "my_histogram" : {
      "values" : [0.1, 0.2, 0.3, 0.4, 0.5],  // Values for each bucket. Values in the array are treated as doubles and must be given in increasing order.
      "counts" : [3, 7, 23, 12, 6] // Count for each bucket. Values in the arrays are treated as integers and must be positive or zero.
   }
}

PUT my-index-000001/_doc/2
{
  "my_text" : "histogram_2",
  "my_histogram" : { 
      "values" : [0.1, 0.25, 0.35, 0.4, 0.45, 0.5], 
      "counts" : [8, 17, 8, 7, 6, 2] 
   }
}
```



### multi-fields

It is often useful to index the same field in different ways for different purposes. This is the purpose of *multi-fields*. **Multi-fields do not change the original `_source` field.**

```json
PUT my-index-000001
{
  "mappings": {
    "properties": {
      "city": {
        "type": "text",
        "fields": {
          "raw": { // The `city.raw` field is a keyword version of the city field.
            "type":  "keyword"
          }
        }
      }
    }
  }
}

PUT my-index-000001/_doc/1
{
  "city": "New York"
}

PUT my-index-000001/_doc/2
{
  "city": "York"
}

GET my-index-000001/_search
{
  "query": {
    "match": {
      "city": "york"  // The `city` field can be used for full text search.
    }
  },
  "sort": {
    "city.raw": "asc" // The `city.raw` field can be used for sorting and aggregations
  },
  "aggs": {
    "Cities": {
      "terms": {
        "field": "city.raw" // The `city.raw` field can be used for sorting and aggregations
      }
    }
  }
}
```

### Multi-value fields and the inverted index

The fact that all field types support multi-value fields out of the box is a consequence of the origins of Lucene. Lucene was designed to be a full text search engine. In order to be able to search for individual words within a big block of text, Lucene tokenizes the text into individual terms, and adds each term to the inverted index separately.

This means that even a simple text field must be able to support multiple values by default. When other data types were added, such as numbers and dates, they used the same data structure as strings, and so got multi-values for free.

# 3  ElasticSearch 配置

### 3.1  运行elasticsearch

```sh
./bin/elasticsearch -d   // 后台运行， es 日志文件路径`./logs/`, 

./bin/elasticsearch -d -Ecluster.name=my_cluster -Enode.name=node_1  // es 默认从 `./config/elasticsearch.yml`文件中加载配置。也可使用`-E`在启动时配置
```

### 3.2 配置文件

##### 3.2.1 jvm.options

一般不建议修改。可以配置内存大小 -Xms

##### 3.2.2 elasticsearch.yml

```yaml
indices.fielddata.cache.size: 12GB  # field data 缓存设置（需要小于field data 短路器的内存限制），默认没有限制（达到一定大小时会触发 field data 短路器）

indices.breaker.fielddata.limit: 40% # field data 短路器的内存限制, 默认大小为堆的40%



```











# 4  Rest API

### 4.1  curl 发送请求

```sh
curl -H "Content-Type: application/json" -X<VERB> '<PROTOCOL>://<HOST>:<PORT>/<PATH>?<QUERY_STRING>' -d '<BODY>'  
# 使用curl向es发送http请求
# -H 添加请求头
# <VERB>表示http方法，如 GET, POST, PUT, HEAD, or DELETE. 
```

### 4.2 日期计算

##### 4.2.1 支持的类型

`y`-`Years`, `M`-`Months`, `w`-`Weeks`, `d` - `Days`, `h`- `Hours`, `H`- `Hours`,`m`-`Minutes`,`s`-`Seconds`

### 4.3 cat API

##### 4.3.1 通用参数

| 参数    | 含义                                                         |
| ------- | ------------------------------------------------------------ |
| v       | 打开`verbose`输出                                            |
| help    | 帮助                                                         |
| h=      | 指定返回的列                                                 |
| bytes=  | 数据单位；`b`-`Bytes`,`kb`-`Kilobytes`,`mb`-`Megabytes`,`gb`-`Gigabytes`,`tb`-`Terabytes`,`pb`-`Petabytes` |
| time=   | 时间单位；`d` - `Day`, `h`- `Hours`,`m`-`Minutes`,`s`-`Seconds`,`ms`-`Milliseconds`, `micros`-`Microseconds`, `nanos` - `Nanoseconds` |
| size=   | 大小单位；`k`-`Kilo`,`m`-`Mega`,`g`-`Giga`,`t`-`Tera`,`p`-`Peta` |
| s=      | 排序                                                         |
| format= | 格式化；`text` (default) -` json` -` smile` - `yaml` - `cbor` |
| pretty  | pretty输出                                                   |

示例：

```json
GET /_cat/templates?v&s=order:desc,index_patterns&format=json&h=name,index*
```



### 4.2  集群

```json
GET /_cat/health?v&pretty  // 查询es集群健康状态；集群状态: red - 数据不可用； yellow - 副本分片不可用；green - 主分片和副本分片都正常
```



### 4.3 索引和文档

```json
// 创建索引
PUT /my-index-000001
{
  "settings": {
    "number_of_shards": 3,   // 3个主分片
    "number_of_replicas": 2   // 每个主分片有2个副本分片
  },
  "mappings": {
    "properties": {
    "field1": 
        { "type": "text" }
    }
  }
}
```

##### 4.3.1 Mapping

`Mapping`定义了文档及其所包含字段的存储和索引方式。由两部分组成：`Metadata fields`， `fields`。

- Metadata fields

    `Metadata fields` 定义了文档的元数据。

- fields

  `fields`定义了文档的字段，每个属性有它自己的数据类型。

```json
// 1.创建索引时显示指定Mapping
PUT /my-index-000001
{
  "mappings": {
    "properties": {
      "age":    { "type": "integer" },  
      "email":  { "type": "keyword"  }, 
      "name":   { "type": "text"  }     
    }
  }
}

// 2.向已存在的索引新增字段
PUT /my-index-000001/_mapping
{
  "properties": {
    "employee-id": {
      "type": "keyword",
      "index": false
    }
  }
}

// 3.对于已存在字段的type不能修改，如果需要修改，新建索引，reindex

// 4.重命名字段会导致旧名称下的索引无效，可以通过给字段起别名来实现重命名。
//   别名可以在创建索引时新建，也可以在创建索引后修改mapping。别名只支持`search`，不能用于`index`和`update`，不能用于`copy_to`的目标。别名在`_source`中没有。
PUT my-index-000001/_mapping
{
  "properties": {
    "alias_name": {
      "type": "alias",
      "path": "employee-id" // 必须是具体的唯一字段且创建别名时已存在，不能是`object`或其他字段的别名。If nested objects are defined, a field alias must have the same nested scope as its target.
    }
  }
}
```

##### 4.3.1.1 mapping parameters

`Mapping parameters` 用于定义字段的`mapping`。

| name              | info                                                         |
| ----------------- | ------------------------------------------------------------ |
| `analyzer`        | 只有`text`类型的字段支持，指定用于`index`和`search`字段时使用的 `text analyzer`。 |
| `search_analyzer` | 默认`index`和`search`时都使用`analyzer`指定的分析器；`search_analyzer`可以单独指定`search`时使用的分析器。 |
| `index`           | 控制字段是否`index`，不被`index`将不可查询。有效值：`true`，`false`。默认`true`。 |
| `boost`           | 默认`1.0`。查询时当前字段对计算`score`的权重倍数。也可在查询的时候指定`boost`查询参数（建议查询时指定，而不是`index`时指定）。`The boost is applied only for term queries (prefix, range and fuzzy queries are not boosted).` |
| `coerce`          | 有效值：`true`，`false`。                                    |
|                   |                                                              |
|                   |                                                              |

```json
// 验证 analyzer
POST _analyze
{
  "analyzer": "standard",  // analyzer 名称
  "text": "A Quick Brown Fox."  // 用于测试的 text 文本
}
```

```json
PUT my-index-000001
{
   "settings":{
      "analysis":{
         "analyzer":{
            "my_analyzer":{ 
               "type":"custom",
               "tokenizer":"standard",
               "filter":[
                  "lowercase"
               ]
            },
            "my_stop_analyzer":{ 
               "type":"custom",
               "tokenizer":"standard",
               "filter":[
                  "lowercase",
                  "english_stop"
               ]
            }
         },
         "filter":{
            "english_stop":{
               "type":"stop",
               "stopwords":"_english_"
            }
         }
      }
   },
   "mappings":{
       "properties":{
          "title": {
             "type":"text",
             "analyzer":"my_analyzer", 
             "search_analyzer":"my_stop_analyzer", 
             "search_quote_analyzer":"my_analyzer" // 用于pharse queries
         }
      }
   }
}

PUT my-index-000001/_doc/1
{
   "title":"The Quick Brown Fox"
}

PUT my-index-000001/_doc/2
{
   "title":"A Quick Brown Fox"
}

GET my-index-000001/_search
{
   "query":{
      "query_string":{
         "query":"\"the quick brown fox\""  // pharse queries
      }
   }
}
```

```json
// index 时指定 boost， 不建议使用
PUT my-index-000001
{
  "mappings": {
    "properties": {
      "title": {
        "type": "text",
        "boost": 2 
      },
      "content": {
        "type": "text"
      }
    }
  }
}

// 查询时指定 boost，作为index时指定的替代
POST _search
{
  "query": {
    "match": {
      "title": {
        "query": "quick brown fox",
        "boost": 2
      }
    }
  }
}

```

```json
PUT my-index-000001
{
  "mappings": {
    "properties": {
      "number_one": {
        "type": "integer"
      },
      "number_two": {
        "type": "integer",
        "coerce": false
      }
    }
  }
}

PUT my-index-000001/_doc/1
{
  "number_one": "10"  // success
}

PUT my-index-000001/_doc/2
{
  "number_two": "10"  // error
}

PUT my-index-000001/_doc/3
{ "number_one": "10.1" }  // success
```



##### 4.3.2 Index API

```json
PUT /<target>/_doc/<_id>

// 自动生成文档id
POST /<target>/_doc/

// target: 如果索引不存在，自动创建索引
// _doc: 默认的type名
// _id: 文档的唯一id
```

```json
// 示例1

// 查询参数：
//    op_type: 可选，有效值：index、create. 默认值 index. 
//             create - 只有当doc id 不存在时才会index, 否则操作失败。index - doc id 不存在新增，存在时更新（先删后增，会导致以前的部分字段丢失）
//    routing: 指向主分配的路由
//    require_alias： 有效值：true、false. 默认 false. 
//             true - 提供的target必须是索引别名        
PUT /customer/_doc/1  // 索引名（如果索引不存在会自动创建）/ type（7.10默认type名是_doc）/ 文档唯一id
{
  "name": "John Doe"
}

// 请求返回
{
  "_index" : "customer", // index name
  "_type" : "_doc",  // type name
  "_id" : "1",      // doc id
  "_version" : 1,      // 版本号，文档每次更新增加1
  "result" : "created",  // index的result有两种：created, updated
  "_shards" : {  // 分片
    "total" : 2,
    "successful" : 2,
    "failed" : 0
  },
  "_seq_no" : 26,  // index操作时会分配一个 seq_no，保证旧版本的文档不会重写新版本的文档
  "_primary_term" : 4
}
```



### 4.4 文档查询

```json
// 查询文档
GET /customer/_doc/1	

// 调用返回
{
  "_index" : "customer",
  "_type" : "_doc",
  "_id" : "1",
  "_version" : 1,
  "_seq_no" : 26,
  "_primary_term" : 4,
  "found" : true,
  "_source" : {    // fields 集合
    "name": "John Doe"
  }
}
```

```json
// _search 
GET /bank/_search
{
  "query": { "match_all": {} },
  "sort": [ // 默认按照相关性分数由高到低排序
    { "account_number": "asc" }
  ],
  "from": 10,
  "size": 10  
}

//请求返回
{
  "took" : 63,   // elasticsearch 执行查询请求耗时 63ms
  "timed_out" : false,
  "_shards" : {
    "total" : 5,  // 总共查询5个分片
    "successful" : 5,  // 5个分片成功
    "skipped" : 0,   // 0个分片跳过
    "failed" : 0    // 0个分片失败
  },
  "hits" : {
    "total" : {  
        "value": 1000,   // 总共有1000个匹配到的文档
        "relation": "eq"   
    },
    "max_score" : null,  // 查询到的相关文档的最高分
    "hits" : [ {               // hits 返回匹配查询条件的文档。不指定from，size时默认返回10条
      "_index" : "bank",
      "_type" : "_doc",
      "_id" : "0",
      "sort": [0],  // 文档排序位置（不使用相关性分数排序时有效）
      "_score" : null,   // 文档的相关分数，使用`match_all`时不可用
      "_source" : {"account_number":0,"balance":16623,"firstname":"Bradshaw","lastname":"Mckenzie","age":29,"gender":"F","address":"244 Columbus Place","employer":"Euron","email":"bradshawmckenzie@euron.com","city":"Hobucken","state":"CO"}
    }, {
      "_index" : "bank",
      "_type" : "_doc",
      "_id" : "1",
      "sort": [1],
      "_score" : null,
      "_source" : {"account_number":1,"balance":39225,"firstname":"Amber","lastname":"Duke","age":32,"gender":"M","address":"880 Holmes Lane","employer":"Pyrami","email":"amberduke@pyrami.com","city":"Brogan","state":"IL"}
    }, ...
    ]
  }
}
```

##### 4.4.1 match_phrase and match

```json
GET /bank/_search
{
  "query": { "match": { "address": "mill lane" } } // 查询address字段中包含`mill` 或 `lane`的 customers
}
```

```json
GET /bank/_search
{
  "query": { "match_phrase": { "address": "mill lane" } } // 查询address字段中包含`mill lane`的 customers
}
```



##### 4.4.2 bool 查询

```json
GET /bank/_search
{
  "query": {
    "bool": {
      "must": [
        { "match": { "age": "40" } }
      ],
      "must_not": [
        { "match": { "state": "ID" } }
      ]
    }
  }
}
```

**`should`, `must` 影响相关性得分（`relevance score`）；`must_not`相当于`filter`，只决定结果是否包括某些文档，不影响 score。**

```json 
GET /bank/_search
{
  "query": {
    "bool": {
      "must": { "match_all": {} },
      "filter": { 
        "range": {  // range filter
          "balance": {
            "gte": 20000,
            "lte": 30000
          }
        }
      }
    }
  }
}
```

### 4.5 aggregation  聚合

##### 4.5.1 terms aggregation

分组统计

```json
GET /bank/_search
{  // 按照 state.keyword 字段对`bank`索引的所有文档进行分组
  "size": 0, // 不返回hits结果
  "aggs": {  // 聚合
    "group_by_state": {  // 聚合名
      "terms": {  // 聚合类型
        "field": "state.keyword" // 分组使用的字段
      }
    }
  }
}

// 调用返回
{
  "took": 29,
  "timed_out": false,
  "_shards": {
    "total": 5,
    "successful": 5,
    "skipped" : 0,
    "failed": 0
  },
  "hits" : {
     "total" : {
        "value": 1000,
        "relation": "eq"
     },
    "max_score" : null,
    "hits" : [ ]
  },
  "aggregations" : {
    "group_by_state" : {
      "doc_count_error_upper_bound": 20,
      "sum_other_doc_count": 770,
      "buckets" : [ {  // buckets 显示terms aggregation 结果， 默认返回前10条（按照doc_count降序）
        "key" : "ID",  // 分组字段值
        "doc_count" : 27  // 当前字段值的文档数量
      }, {
        "key" : "TX",
        "doc_count" : 27
      }, {
        "key" : "AL",
        "doc_count" : 25
      }, {
        "key" : "MD",
        "doc_count" : 25
      }, {
        "key" : "TN",
        "doc_count" : 23
      }, {
        "key" : "MA",
        "doc_count" : 21
      }, {
        "key" : "NC",
        "doc_count" : 21
      }, {
        "key" : "ND",
        "doc_count" : 21
      }, {
        "key" : "ME",
        "doc_count" : 20
      }, {
        "key" : "MO",
        "doc_count" : 20
      } ]
    }
  }
}
```

##### 4.5.2 metrics aggregations

度量统计

- `avg`：
- `sum`：

#####  

##### 4.5.3 聚合的组合使用

```json
GET /bank/_search
{
  "size": 0,
  "aggs": {
    "group_by_state": {
      "terms": {
        "field": "state.keyword",
        "order": {
          "average_balance": "desc"
        }
      },
      "aggs": {
        "average_balance": {
          "avg": {
            "field": "balance"
          }
        }
      }
    }
  }
}
```





# Reference

\[1\]:[系统学习ElasticSearch](https://www.zhihu.com/column/TeHero)
\[2\]:[ElasticSearch文档](https://www.elastic.co/guide/en/elasticsearch/reference/7.9/index.html)
\[3\]:[Elasticsearch 6.0 一个索引只允许有一个type](https://elasticsearch.cn/article/337)