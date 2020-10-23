# 思维导图


![img](E:\GitRepository\test\image\v2-5b3f5e22445109e74e3e67fa3f4556a5_720w.jpg)

![img](E:\GitRepository\test\image\v2-740d6b993e94def9fd84547fe4ef098a_720w.jpg)

![img](E:\GitRepository\test\image\v2-7bf3269cbc937cd64d0a215275afc6f2_720w.jpg)

![img](E:\GitRepository\test\image\v2-bb2d3723ea06097bdca2eecfb2d0e91b_720w.jpg)

![img](E:\GitRepository\test\image\v2-03b12f7b41bbfb450dcf19334c5af50c_720w.jpg)

![img](E:\GitRepository\test\image\v2-69ce1243e44a0970718cb070ef7f3ab8_720w.jpg)

# 概念

Cluster, node, index, shard, mapping, type, document, field.

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

# 数据类型

本节中请求示例基于 `elasticsearch 7.9`，`7.0`之前的版本`mapping`的定义需要包含`type`的名称。

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
| search_analyzer |The analyzer that should be used at search time on the text field. Defaults to the analyzer setting.|
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

# Rest API



# Reference

\[1\]:[系统学习ElasticSearch](https://www.zhihu.com/column/TeHero)
\[2\]:[ElasticSearch文档](https://www.elastic.co/guide/en/elasticsearch/reference/7.9/index.html)
\[3\]:[Elasticsearch 6.0 一个索引只允许有一个type](https://elasticsearch.cn/article/337)