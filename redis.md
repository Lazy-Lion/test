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

#### Redis keys
Redis keys are binary safe, this means that you can use any binary sequence as a key, from a string like "foo" to the content of a JPEG file. **The empty string is also a valid key.** The maximum allowed key size is 512 MB.

#### 数据类型
| Type | Info | Command |
| - | - | - |
| String | Strings are the most basic kind of Redis value. Redis Strings are binary safe, this means that a Redis string can contain any kind of data, for instance a JPEG image or a serialized Ruby object.A String value can be at max 512 Megabytes in length. | GET, SET, MSET, MGET, APPEND, STRLEN, INCR, DECR, INCRBY, DECRBY, GETSET| 
| Hash | A Redis hash is a collection of key value pairs. Redis Hashes are maps between string fields and string values, so they are the perfect data type to represent objects. Every hash can store up to 2^32 - 1 field-value pairs (more than 4 billion). | HMSET, HGETALL, HSET, HGET, HDEL, HEXISTS | 
| List | Redis Lists are simply lists of strings, sorted by insertion order. **They are basically linked lists.** You can add elements to a Redis List on the head or on the tail. The max length of a list is 2^32 - 1 elements. | LPUSH, RPUSH, LRANGE, LINDEX, BLPOP, LPOP | 
| Set | Redis Sets are an unordered collection of Strings. Redis Sets have the desirable property of not allowing repeated members. The max number of members in a set is 2^32 - 1. | SADD, SCARD, SREM, SMOVE |
| Sorted Set | Redis Sorted Sets are, similarly to Redis Sets, non repeating collections of Strings. The difference is that every member of a Sorted Set is associated with **score(64 bits double)**, that is used in order to take the sorted set ordered, from the smallest to the greatest score. While members are unique, scores may be repeated. If A and B have exactly the same score, then A > B if the A string is lexicographically greater than the B string. | ZADD, ZCARD, ZCOUNT, ZRANK |
| HyperLogLog |  | PFADD, PFCOUNT, PFMERGE |
| BitMap | | |

#### -inf , +inf

## 命令
 | Data Type | Command | Info |
 | - | - | - |
 | | MULTI/EXEC | MULTI marks the start of transaction block, EXEC executes all previously queued commands in a transaction and restores the connection state to normal. |
 | | EXISTS | Returns if key exists |
 | | GETSET | Sets a key to a new value, returning the old value as the result |
 | | SETNX | set if not exists |
 | | INCR | Increments the number stored at key by one (**atomic operation**). This operation is limited to **64 bit signed integers(actually a String operation,  Redis does not have a dedicated Integer type)**. |
 | | DECR | Decrements the number stored at key by one (**atomic operation**). |
 | | DEL | Removes the specified keys. A key is ignored if it does not exist. |
 | | TYPE | Returns the string representation of the type of the value stored at key. The different types that can be returned are: string, list, set, zset and hash. |
 | | EXPIRE | Set a timeout on key. Another way to set expire : set key 100 ex 10 (have an expire of ten seconds) |
 | | PEXPIRE | Work exactly like EXPIRE but the time to live of the key is specified in milliseconds instead of seconds. |
 | | PERSIST | Remove the existing timeout on key, turning the key from volatile (a key with an expire set) to persistent (a key that will never expire as no timeout is associated). |
 | | TTL | Returns the remaining time to live of a key that has a timeout. |
 | | PTTL | Like TTL, Milliseconds instead of seconds. | 
 | List | LLEN | Returns the length of the list stored at key. If key does not exist, it is interpreted as an empty list and 0 is returned. An error is returned when the value stored at key is not a list. |
 | | LPUSH | Insert all the specified values at the head of the list stored at key. |
 | | RPUSH | Insert all the specified values at the tail of the list stored at key. For example, **RPUSH mylist 1 2 3 4 5 6**| 
 | | LRANGE | Returns the specified elements of the list stored at key. The offsets start and stop are zero-based indexes, with 0 being the first element of the list (the head of the list), 1 being the next element and so on. The offsets can be nagative numbers, for example, -1 is the last element of the list, -2 is the penultimate element of the list. **"LRANGE list 0 10" will return 11 elements.** Out of range indexes will not produce an error. |
 | | RPOP | Removes and returns the last element of the list stored at key. |
 | | LPOP | Removes and returns the first element of the list stored at key. |
 | | LREM | **LREM key count value** . Removes the first count occurrences of elements equal to value from the list stored at key. <br /> 1) count > 0: Remove count elements equal to value moving from head to tail. <br />2) count < 0: Remove -count elements equal to value moving from tail to head. <br />3) count = 0: Remove all elements equal to value.|
 | | LTRIM | Trim an existing list so that it will contain only the specified range of elements specified, all the elements outside the given range are removed. The offsets are like LRANGE.|
 | | RPOPLPUSH | **RPOPLPUSH source destination** . Atomically returns and removes the last element (tail) of the list stored at source, and pushes the element at the first element (head) of the list stored at destination. |
 | | BLPOP | The blocking version of LPOP because it blocks the connection when there are no elements to pop from any of the given lists. Return: 1) A nil multi-bulk when no element could be popped and the timeout expired. 2) A two-element multi-bulk with the first element being the name of the key where an element was popped and the second element being the value of the popped element. | 
 | | BRPOP | Be like BLPOP |
 | | BRPOPLPUSH | It is the blocking variant of RPOPLPUSH.When source is empty, Redis will block the connection until another client pushes to it or until timeout is reached. **A timeout of zero can be used to block indefinitely.** |
 | Hash | HMSET | Sets multiple fields of the hash |
 | | HGET | Returns the value associated with field in the hash stored at key. |
 | | HMGET | **HMGET key field \[field ...\]** |
 | | HGETALL | Returns all fields and values of the hash stored at key. |
 | Set | SADD | Add the specified members to the set stored at key. Specified members that are already a member of this set are ignored. |
 | | SPOP | **SPOP key \[count\]** . Removes and returns one or more random elements from the set value store at key. |
 | | SMEMBERS | Returns all the members of the set value stored at key. | 
 | | SISMEMBER | Returns if member is a member of the set stored at key. | 
 | | SINTER | Returns the members of the set resulting from the intersection of all the given sets. | 
 | | SINTERSTORE | **SINTERSTORE destination key \[key ...\]** . This command is equal to SINTER, but instead of returning the resulting set, it is stored in destination. **If destination already exists, it is overwritten.** |
 | | SUNION | Returns the members of the set resulting from the union of all the given sets. |
 | | SUNIONSTORE | |
 | | SDIFF | Returns the members of the set resulting from the difference between the first set and all the successive sets. |
 | | SDIFFSTORE | |
 | | SCARD | Returns the set cardinality (number of elements) of the set stored at key. | 
 | | SRANDMEMBER | **SRANDMEMBER key \[count\]** <br /> 1) count is positive : return an array of count **distinct elements**. <br /> 2) count is nagative : return an array of -count elements, is allowed to return **the same element multiple times**. <br /> 3) no count argument : return a random element | 
 | Sorted Set | ZADD | **ZADD key \[NX\|XX\] \[CH\] \[INCR\] score member \[score member ...\]** . <br /> 1)XX: Only update elements that already exist. Never add elements.<br /> 2)NX: Don't update already existing elements. Always add new elements.<br /> 3)CH: Modify the return value from the number of new elements added, to the total number of elements changed (CH is an abbreviation of changed). Changed elements are new elements added and elements already existing for which the score was updated. So elements specified in the command line having the same score as they had in the past are not counted. Note: normally the return value of ZADD only counts the number of new elements added.<br /> 4)INCR: When this option is specified ZADD acts like ZINCRBY. Only one score-element pair can be specified in this mode. |
 | | ZINCRBY | **ZINCRBY key increment member** .Increments the score of member in the sorted set stored at key by increment. |
 | | ZSCORE | Returns the score of member in the sorted set at key. If member does not exist in the sorted set, or key does not exist, nil is returned. |
 | | ZRANGE | **ZRANGE key start stop \[WITHSCORES\]** .Returns the specified range (ascending) of elements in the sorted set stored at key.  |
 | | ZREVRANGE | Returns the specified range (descending) of elements in the sorted set stored at key. |
 | | ZRANGEBYSCORE | **ZRANGEBYSCORE key min max \[WITHSCORES\] \[LIMIT offset count\]** . By default, the interval specified by min and max is closed (inclusive). It is possible to specify an open interval (exclusive) by prefixing the score with the character ( . For example : **zrangebyscore zset (1 (5**. |
 | | ZREMRANGEBYSCORE | **ZREMRANGEBYSCORE key min max**. Removes all elements in the sorted set stored at key with a score between min and max (inclusive). |
 | | ZRANK | |
 | | ZREVRANK | |
 | | ZRANGEBYLEX | |
 | | ZREVRANGEBYLEX | |
 | | ZREMRANGEBYLEX | |
 | | ZLEXCOUNT | |
 
 
 

## Automatic creation and removal of keys
- When we add an element to an aggregate data type, if the target key does not exist, an empty aggregate data type is created before adding the element.
- When we remove elements from an **aggregate data type (List, Hash, Set, Sorted Set)**, if the value remains empty, the key is automatically destroyed.
- Calling a read-only command such as LLEN (which returns the length of the list), or a write command removing elements, with an empty key, always produces the same result as if the key is holding an empty aggregate type of the type the command expects to find. 

## References
\[1\]:[An Introduction to Redis Types and Abstractions](https://redis.io/topics/data-types-intro)<br />
\[2\]:[Redis Commands](https://redis.io/commands) <br />
\[3\]:[Memcached vs Redis](https://www.linkedin.com/pulse/memcached-vs-redis-which-one-pick-ranjeet-vimal)<br />
\[4\]:[Redis命令参考](http://doc.redisfans.com/)<br />
\[5\]:[Try Redis](http://try.redis.io/)
