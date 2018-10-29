## linux下安装redis
```
$ wget http://download.redis.io/releases/redis-4.0.9.tar.gz
$ tar xzf redis-4.0.9.tar.gz
$ cd redis-4.0.9
$ make

//启动 redis 服务
$ cd src
$ ./redis-server

//测试客户端
$ cd src 
$ ./redis-cli

//配置文件 redis.conf 在 redis-4.0.9 文件夹下

```

## 数据类型

| Type | Info | Command |
| - | - | - |
| String | Strings are the most basic kind of Redis value. Redis Strings are binary safe, this means that a Redis string can contain any kind of data, for instance a JPEG image or a serialized Ruby object.A String value can be at max 512 Megabytes in length. | GET, SET, MSET, MGET, APPEND, STRLEN | 
| Hash | A Redis hash is a collection of key value pairs. Redis Hashes are maps between string fields and string values, so they are the perfect data type to represent objects. Every hash can store up to 2^32 - 1 field-value pairs (more than 4 billion). | HMSET, HGETALL, HSET, HGET, HDEL, HEXISTS | 
| List | Redis Lists are simply lists of strings, sorted by insertion order. They are basically linked lists. You can add elements to a Redis List on the head or on the tail. The max length of a list is 2^32 - 1 elements. | LPUSH, RPUSH, LRANGE, LINDEX, BLPOP, LPOP | 
| Set | Redis Sets are an unordered collection of Strings. Redis Sets have the desirable property of not allowing repeated members. The max number of members in a set is 2^32 - 1. | SADD, SCARD, SREM, SMOVE |
| Sorted Set | Redis Sorted Sets are, similarly to Redis Sets, non repeating collections of Strings. The difference is that every member of a Sorted Set is associated with score, that is used in order to take the sorted set ordered, from the smallest to the greatest score. While members are unique, scores may be repeated. | ZADD, ZCARD, ZCOUNT, ZRANK |
| HyperLogLog |  | PFADD, PFCOUNT, PFMERGE |
| BitMap | | |

[Redis Commands](https://redis.io/commands) <br />


