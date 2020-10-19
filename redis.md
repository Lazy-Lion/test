---
typora-copy-images-to: image
---

Redis 是单进程、单线程的
Nginx是多进程、单线程的
Memcached是单进程、多线程的

# linux下安装redis
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

# 数据类型

### Redis keys
Redis keys are binary safe, this means that you can use any binary sequence as a key, from a string like "foo" to the content of a JPEG file. **The empty string is also a valid key.** The maximum allowed key size is 512 MB.

### 数据类型
| Type | Info | Command |
| - | - | - |
| String | Strings are the most basic kind of Redis value. Redis Strings are binary safe, this means that a Redis string can contain any kind of data, for instance a JPEG image or a serialized Ruby object.A String value can be at max 512 Megabytes in length. | GET, SET, MSET, MGET, APPEND, STRLEN, INCR, DECR, INCRBY, DECRBY, GETSET|
| Hash | A Redis hash is a collection of key value pairs. Redis Hashes are maps between string fields and string values, so they are the perfect data type to represent objects. Every hash can store up to 2^32 - 1 field-value pairs (more than 4 billion). | HMSET, HGETALL, HSET, HGET, HDEL, HEXISTS |
| List | Redis Lists are simply lists of strings, sorted by insertion order. **They are basically linked lists.** You can add elements to a Redis List on the head or on the tail. The max length of a list is 2^32 - 1 elements. | LPUSH, RPUSH, LRANGE, LINDEX, BLPOP, LPOP |
| Set | Redis Sets are an unordered collection of Strings. Redis Sets have the desirable property of not allowing repeated members. The max number of members in a set is 2^32 - 1. | SADD, SCARD, SREM, SMOVE |
| Sorted Set | Redis Sorted Sets are, similarly to Redis Sets, non repeating collections of Strings. The difference is that every member of a Sorted Set is associated with **score(64 bits double)**, that is used in order to take the sorted set ordered, from the smallest to the greatest score. While members are unique, scores may be repeated. If A and B have exactly the same score, then A > B if the A string is lexicographically greater than the B string. | ZADD, ZCARD, ZCOUNT, ZRANK |
| HyperLogLog |  | PFADD, PFCOUNT, PFMERGE |
| BitMap | | |

### -inf , +inf

# 命令
| Data Type | Command | Info |
| - | - | - |
| | MULTI/EXEC | MULTI marks the start of transaction block, EXEC executes all previously queued commands in a transaction and restores the connection state to normal. |
| | EXISTS | Returns if key exists |
| | GETSET | Sets a key to a new value, returning the old value as the result |
| | SETNX | set if not exists |
| | INCR | Increments the number stored at key by one (**atomic operation**). This operation is limited to **64 bit signed integers(actually a String operation,  Redis does not have a dedicated Integer type)**. |
| | DECR | Decrements the number stored at key by one (**atomic operation**). |
| | DEL | Removes the specified keys. A key is ignored if it does not exist. |
| | [SCAN](https://redis.io/commands/scan) | **SCAN cursor \[MATCH pattern\] \[COUNT count\]** |
| | KEYS | **KEYS pattern**. Returns all keys matching pattern. Pattern : h?llo, h\*llo, h\[ae\]llo, h\[^e\]llo, h\[a-b\]llo |
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
| | HSCAN | |
| Set | SADD | Add the specified members to the set stored at key. Specified members that are already a member of this set are ignored. |
| | SPOP | **SPOP key \[count\]** . Removes and returns one or more random elements from the set value store at key. |
| | SMEMBERS | Returns all the members of the set value stored at key. |
| | SSCAN | |
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
| | ZCARD | **ZCARD key**. Returns the sorted set cardinality (number of elements) of the sorted set stored at key. |
| | ZCOUNT | **ZCOUNT key min max**. Returns the number of elements in the sorted set at key with a score between min and max. |
| | ZINCRBY | **ZINCRBY key increment member** .Increments the score of member in the sorted set stored at key by increment. |
| | ZSCORE | Returns the score of member in the sorted set at key. If member does not exist in the sorted set, or key does not exist, nil is returned. |
| | ZRANGE | **ZRANGE key start stop \[WITHSCORES\]** .Returns the specified range (ascending) of elements in the sorted set stored at key.  |
| | ZREVRANGE | Returns the specified range (descending) of elements in the sorted set stored at key. |
| | ZRANGEBYSCORE | **ZRANGEBYSCORE key min max \[WITHSCORES\] \[LIMIT offset count\]** . By default, the interval specified by min and max is closed (inclusive). It is possible to specify an open interval (exclusive) by prefixing the score with the character ( . For example : **zrangebyscore zset (1 (5**. |
| | ZREMRANGEBYSCORE | **ZREMRANGEBYSCORE key min max**. Removes all elements in the sorted set stored at key with a score between min and max (inclusive). |
| | ZRANK | Determine the index of a member in a sorted set. |
| | ZREVRANK | Determine the index of a member in a sorted set, with scores ordered from high to low. |
| | ZRANGEBYLEX | **ZRANGEBYLEX key min max \[LIMIT offset count\]**. Return a range of members in a sorted set, by lexicographical range. If the elements in the sorted set have different scores, the returned elements are unspecified. **Valid start and stop must start with ( or \[**, in order to specify if the range item is respectively exclusive or inclusive. The special values of + or - for start and stop have the special meaning or positively infinite and negatively infinite strings. |
| | ZREVRANGEBYLEX | **ZREVRANGEBYLEX key max min \[LIMIT offset count\]**. Return a range of members in a sorted set, by lexicographical range, ordered from higher to lower strings. |
| | ZREMRANGEBYLEX | **ZREMRANGEBYLEX key min max**. Remove all members in a sorted set between the given lexicographical range. The meaning of min and max are the same of the ZRANGEBYLEX command. |
| | ZLEXCOUNT | **ZLEXCOUNT key min max**. Count the number of members in a sorted set between the given lexicographical range. The min and max arguments have the same meaning as described for ZRANGEBYLEX. |
| | ZSCAN | **ZSCAN key cursor \[MATCH pattern\] \[COUNT count\]** |


# Automatic creation and removal of keys
- When we add an element to an **aggregate data type(List, Hash, Set, Sorted Set)**, if the target key does not exist, an empty aggregate data type is created before adding the element.
- When we remove elements from an **aggregate data type**, if the value remains empty, the key is automatically destroyed.
- Calling a read-only command such as LLEN (which returns the length of the list), or a write command removing elements, with an empty key, always produces the same result as if the key is holding an empty aggregate type of the type the command expects to find.



# Redis持久化之RDB和AOF

RDB(Redis DataBase), AOF(Append Only File)

RDB 是 Redis 默认的持久化方案。在指定的时间间隔内，执行指定次数的写操作，则会将内存中的数据写入到磁盘中。即在指定目录下生成一个dump.rdb文件。Redis 重启会通过加载dump.rdb文件恢复数据。<br />

AOF: Redis 默认不开启。它的出现是为了弥补RDB的不足（数据的不一致性），所以它采用日志的形式来记录每个写操作，并追加到文件中。Redis 重启的会根据日志文件的内容将写指令从前到后执行一次以完成数据的恢复工作。

# Redis事务

Redis通过MULTI、EXEC、WATCH等命令来实现事务机制，事务执行过程将一系列命令按照顺序一次性执行，并且在执行期间，事务不会被中断，也不会去执行客户端的其他请求，直到所有命令执行完毕。事务的执行过程如下：

1. 服务端收到客户端请求，事务以MULTI开始
2. 如果客户端正处于事务状态，则会把事务放入队列同时返回给客户端QUEUED，反之则直接执行这个命令
3. 当收到客户端EXEC命令时，WATCH命令监视整个事务中的key是否有被修改，如果有则返回空客户端表示失败，否则redis会遍历整个事务队列，执行队列中保存的所有命令，最后返回结果给客户端

WATCH的机制本身是一个CAS的机制，被监视的key会被保存到一个链表中，如果某个key被修改，那么REDIS_DIRTY_CAS 标志将会被打开，这时服务器会拒绝执行事务。

# Redis 发布订阅模式

Redis 通过 PUBLISH 、 SUBSCRIBE、 UNSUBSCRIBE、 PUNSUBSCRIBE 等命令实现了订阅与发布模式。

### 频道的订阅和信息发送

![digraph pubsub_relation](https://redisbook.readthedocs.io/en/latest/_images/graphviz-58f7b1f1f52b28f59291d194555fc9f4b1462a4c.svg)

![digraph send_message_to_subscriber](https://redisbook.readthedocs.io/en/latest/_images/graphviz-84c95abf88d6c0ac55b007da08805a4b9a582fdf.svg)

### 模式的订阅和信息发送

![digraph pattern_relation ](https://redisbook.readthedocs.io/en/latest/_images/graphviz-49c2b60cc3c2b52ec1623fbd8a9002eb6f335a54.svg)

![digraph pattern_relation](https://redisbook.readthedocs.io/en/latest/_images/graphviz-ba8c4d4dd538464659aeb52d6c366f23ad3d0dc1.svg)



### redis使用链表实现发布订阅模式

![digraph pubsub_pattern](https://redisbook.readthedocs.io/en/latest/_images/graphviz-a84f3abf466ca19297faaa4e11d37f9257355c60.svg)

# Redis 主从复制

Master（主）, Slave（从）, Sentinel（哨兵） <br />

info replication 命令查询主从复制信息
SLAVEOF ip port 命令设置主从关系（设置当前redis为指定redis的从库）
SLAVEOF no one 从库执行该命令可以断开主从关系

Sentinel的任务
 - 监控：哨兵会不断地检查你的Master和Slave是否运作正常
 - 提醒：当被监控的某个Redis出现问题时,哨兵可以通过API向管理员或者其他应用程序发送通知
 - 故障迁移：若一台主机出现问题时，哨兵会自动将该主机下的某一个从机设置为新的主机，并让其他从机和新主机建立主从关系。

主从复制的原理：
 - 全量复制，实现原理：建立主从关系时，从机会给主机发送sync命令，主机接收命令，后台启动存盘进程，同时收集所有用于修改命令，传送给从机。
 - 增量复制，实现原理：主机会继续将新收集到的修改命令依次传给从机，实现数据的同步效果。

Redis的主从复制最大的缺点就是延迟。

# Redis 集群

### distributed system
A *distributed system* is a system whose components are located on different networked computers, which communicate and coordinate their actions by passing messages to one another. The components interact with one another in order to achieve a common goal. Three significant characteristics of distributed systems are: concurrency of components, lack of a global clock, and independent failure of components.

### High-availability clusters 
High-availability clusters (also known as HA clusters , fail-over clusters or Metroclusters Active/Active) are groups of computers that support server applications that can be reliably utilized with a minimum amount of down-time. They operate by using high availability software to harness redundant computers in groups or clusters that provide continued service when system components fail.

Redis 3.0 之后便支持集群。Redis 集群中内置了 16384个哈希槽（Redis集群没有使用一致性哈希）。Redis会根据节点数量大致均等的将哈希槽映射到不同的节点。所有节点之间彼此互联(PING-PONG机制)，当超过半数的主机认为某台主机挂了，则该主机就是真的挂掉了，整个集群就不可用了。

Redis 集群部署方式大部分采用类 Twemproxy 的方式进行部署。即通过 Twemproxy 对 redis key 进行分片计算，将 redis key 进行分片计算，分配到多个 redis 实例中的其中一个。tewmproxy 架构图如下：

![img](https://pic2.zhimg.com/80/v2-4d49e6488657617fab11424816762721_720w.jpg)

### hot key 问题

 For Redis, frequent access of the same key in a **partition** is known as a hotspot key.

##### Common Causes of Hotspot Keys

- The size of user consumption data is much greater than that of production data, and includes hot items, hot news, hot reviews, and celebrity live broadcasts.
- The number of request slices exceeds the performance threshold of a single server.

##### Impact of the Hotspot Key Problem

![1](https://yqintl.alicdn.com/54b8a91a9c3ed48509293d4d628fbd97039532ef.png)

- Traffic is concentrated, reaching the upper limit of the physical network adapter.
- Too many requests queue up, crashing the sharding service of the cache.
- The database is overloaded, resulting in a service avalanche.

##### Recommended Solutions

###### Server Cache Solution

![2](https://yqintl.alicdn.com/852d1f142467ebb61f1859581bec647554555c01.png)

###### Local Cache Solution

Using the local cache incurs the following problems:

1. Hotspots must be detected in advance.
2. The cache capacity is limited.
3. The inconsistency duration is long.
4. Hotspot keys are incomplete.

###### Read/Write Splitting Solution

![4](https://yqintl.alicdn.com/138234a3d1b7f8219f392d268487c10dc23e5217.png)

SLB: Server Load Balancing，负载均衡。

###### Hotspot Data Solution

![5](https://yqintl.alicdn.com/da89997ca5286f4099d58e1b42f30de89c4c95e9.png)

### big key 问题 

Big key 指数据量大的 key。

解决方法： 对 big key 存储的数据 （big value）进行拆分。

# 缓存穿透、缓存击穿、缓存雪崩
### 缓存穿透 
查询缓存中不存在的数据会导致缓存穿透。
解决方案：

 1. 请求到redis，当redis没有命中该数据时，请求会到达mysql；如果mysql也不存在该数据时，则缓存一个空对象到redis中。（可能会缓存很多值为空的key，占用内存空间。同时Redis有LRU或LFU的内存淘汰策略，可能会将缓存中有价值的数据淘汰掉。对空值设置了时间，可能会导致数据库和redis中在某个时间段的数据不一致。）
 2. 布隆过滤器。使用布隆过滤器判断查询条件是否满足条件
### 缓存击穿 
缓存击穿是缓存穿透的特殊表现之一。当某个数据被高并发访问时，如果这个数据redis的key的突然失效，会导致这些请求同一时间打到数据库，数据库扛不住就会导致系统瘫痪。
解决方案：
 1.热点数据不过期。需要保证数据库和redis的弱一致性（难以做到强一致性）。
 2.分布式锁。当热点key过期，允许这个热点key在redis中查询不到数据时将其中一个请求打到达数据库，但不是并发打到数据库，然后将数据缓存到redis，后面的请求就可以到redis中查询到数据了。（分布式锁实现： redis 或 zookeeper）

### 缓存雪崩
缓存雪崩也是缓存穿透的特殊表现之一。
产生的原因：
 1.缓存过期的时间比较一致，某一时刻key大面积失效。解决办法：将缓存时间设置成一个随机数。
 2.redis挂了，或因为网络抖动访问不了redis了。解决办法：使用redis集群。

### Redis 速度快
 - redis是纯内存操作：数据存放在内存中，内存的响应时间大约是100纳秒，这是Redis每秒万亿级别访问的重要基础。
 - 非阻塞I/O：Redis采用epoll做为I/O多路复用技术的实现，再加上Redis自身的事件处理模型（Redis基于Reactor模式（事件驱动））将epoll中的连接，读写，关闭都转换为了时间，不在I/O上浪费过多的时间。
 - 单线程避免了线程切换和竞态产生的消耗。

### Redis6.0之后引入多线程

redis还是使用单线程模型来处理客户端的请求，只是使用多线程来处理数据的读写和协议解析，执行命令还是使用单线程。

这样做的目的是因为redis的性能瓶颈在于网络IO而非CPU，使用多线程能提升IO读写的效率，从而整体提高redis的性能。

# Redis 过期策略和内存淘汰策略

### 过期策略

Keys expiring information is stored as absolute Unix timestamps (in milliseconds in case of Redis version 2.6 or greater). This means that the time is flowing even when the Redis instance is not active.

Redis keys are expired in two ways: a passive way, and an active way.

##### passive way

A key is passively expired simply when some client tries to access it, and the key is found to be timed out.

##### active way

Specifically this is what Redis does 10 times per second:

1. Test 20 random keys from the set of keys with an associated expire.
2. Delete all the keys found expired.
3. If more than 25% of keys were expired, start again from step 1.

In order to obtain a correct behavior without sacrificing consistency, when a key expires, a DEL operation is synthesized in both the AOF file and gains all the attached replicas nodes. This way the expiration process is centralized in the master instance, and there is no chance of consistency errors.

However while the replicas connected to a master will not expire keys independently (but will wait for the DEL coming from the master), they'll still take the full state of the expires existing in the dataset, so when a replica is elected to master it will be able to expire the keys independently, fully acting as a master.

### 内存淘汰策略（Eviction policies）

The exact behavior Redis follows when the `maxmemory` limit is reached is configured using the `maxmemory-policy` configuration directive.

- noeviction: return errors when the memory limit was reached and the client is trying to execute commands that could result in more memory to be used (most write commands, but DEL and a few more exceptions).
- allkeys-lru: evict keys by trying to remove the less recently used (LRU) keys first, in order to make space for the new data added.
- volatile-lru: evict keys by trying to remove the less recently used (LRU) keys first, but only among keys that have an **expire set**, in order to make space for the new data added.
- allkeys-random: evict keys randomly in order to make space for the new data added.
- volatile-random: evict keys randomly in order to make space for the new data added, but only evict keys with an **expire set**.
- volatile-ttl: evict keys with an **expire set**, and try to evict keys with a shorter time to live (TTL) first, in order to make space for the new data added.

# Unix 的 IO 模型

### 阻塞式IO模型

![img](https://upload-images.jianshu.io/upload_images/9021696-96a331dfaf2275f3.png?imageMogr2/auto-orient/strip|imageView2/2/w/950/format/webp)

应用进程调用recvfrom，然后切换到内核空间中运行，直到数据报到达且被复制到应用进程缓冲区中才返回。

### 非阻塞式IO模型

![img](https://upload-images.jianshu.io/upload_images/9021696-34c78c1ae51729bc.png?imageMogr2/auto-orient/strip|imageView2/2/w/932/format/webp)

Non-blocking IO用户进程需要不断的主动询问内核数据好了没有（轮询）。

### IO多路复用模型（IO Multiplexing）

select, poll, epoll

![img](https://upload-images.jianshu.io/upload_images/9021696-7ab52421bcfa275d.png?imageMogr2/auto-orient/strip|imageView2/2/w/953/format/webp)

所以，I/O 多路复用是一个进程能同时等待多个文件描述符，而这些文件描述符（套接字描述符）其中的任意一个进入读就绪状态，select()函数就可以返回。

select/epoll的优势并不是对于单个连接能处理得更快，而是在于能处理更多的连接。

### 信号驱动IO模型

![img](https://upload-images.jianshu.io/upload_images/9021696-dc50b8464d88fb3a.png?imageMogr2/auto-orient/strip|imageView2/2/w/944/format/webp)

### 异步IO模型

![img](https://upload-images.jianshu.io/upload_images/9021696-14dd6d9a3cee6a73.png?imageMogr2/auto-orient/strip|imageView2/2/w/939/format/webp)

与信号驱动模型的主要区别在于：信号驱动式I/O是由内核通知我们何时可以启动一个I/O操作，而异步模型是由内核通知我们I/O操作何时完成。

**非阻塞I/O 系统调用（non-blocking system call）** 和 **异步I/O系统调用（asychronous system call）**的区别是：

- 一个**非阻塞I/O 系统调用 read()** 操作立即返回的是任何可以立即拿到的数据， 可以是完整的结果， 也可以是不完整的结果， 还可以是一个空值。
- 而**异步I/O系统调用read()**结果必须是完整的， 但是这个操作完成的通知可以延迟到将来的一个时间点。

**非阻塞I/O 系统调用（non-blocking system call）**和**异步I/O系统调用** 都是非阻塞式的行为（non-blocking behavior）。 他们的差异仅仅是返回结果的方式和内容不同。

阻塞式IO，非阻塞式IO，IO多路复用，信号驱动IO都是同步IO。

![IO模型对比](https://img-blog.csdn.net/20161021075133062)

### 同步、异步、阻塞、非阻塞

Still another key issue is synchronous (blocking) versus asynchronous (interrupt-driven)transfers. Most physical I/O is asynchronous the CPU starts the transfer and goes off to do something else until the **interrupt** arrives. User programs are much easier to write if the I/O operations are blocking after a receive system call the program is automatically suspended until the data are available in the buffer. It is up to the operating system to make operations that are  actually interrupt-driven look blocking to the user programs.

​                                                                                               *quote from "Operating Systems Design and Implementation"*

<a href="https://www.zhihu.com/question/19732473/answer/88599695">

**CPU层次**
在CPU层次，或者说操作系统进行IO和任务调度的层次，现代操作系统通常使用异步非阻塞方式进行IO（有少部分IO可能会使用同步非阻塞轮询），即发出IO请求之后，并不等待IO操作完成，而是继续执行下面的指令（非阻塞），IO操作和CPU指令互不干扰（异步），最后通过中断的方式来通知IO操作完成结果。

**线程层次**

在线程层次，或者说操作系统调度单元的层次，操作系统为了减轻程序员的思考负担，将底层的异步非阻塞的IO方式进行封装，把相关系统调用（如read，write等）以同步的方式展现出来。然而，同步阻塞的IO会使线程挂起，同步非阻塞的IO会消耗CPU资源在轮询上。为了解决这一问题，就有3种思路：

1. 多线程（同步阻塞）；
2. IO多路复用（select，poll，epoll）（同步非阻塞，严格地来讲，是把阻塞点改变了位置）；
3. 直接暴露出异步的IO接口，如kernel-aio和IOCP（异步非阻塞）。

**程序员感知层次**
在Linux中，上面提到的第2种思路用得比较广泛，也是比较理想的解决方案。然而，直接使用select之类的接口，依然比较复杂，所以各种库和框架百花齐放，都试图对IO多路复用进行封装。此时，库和框架提供的API又可以选择是以同步的**方式**还是异步的**方式**来展现。如python的asyncio库中，就通过协程，提供了同步阻塞式的API；如node.js中，就通过回调函数，提供了异步非阻塞式的API。

# IO多路复用之select, poll, epoll

### Operating System

An **operating system** (**OS**) is system software that manages computer hardware, software resources, and provides common services) for computer programs.

The components of an operating system all exist in order to make the different parts of a computer work together. All user software needs to go through the operating system in order to use any of the hardware, whether it be as simple as a mouse or keyboard or as complex as an Internet component.

Executing an application program involves the creation of a process by the operating system kernel which assigns memory space and other resources, establishes a priority for the process in multi-tasking systems, loads program binary code into memory, and initiates execution of the application program which then interacts with the user and with hardware devices. In modern operating systems, interrupts are handled by the operating system's kernel.

Interrupts are central to operating systems, as they provide an efficient way for the operating system to interact with and react to its environment. Interrupts provide a computer with a way of automatically saving local register contexts, and running specific code in response to events. 

##### hardware interrupt  VS  software interrupt


| **BASIS OF COMPARISON**       | **HARDWARE INTERRUPT**                                       | **SOFTWARE INTERRUPT**                                       |
| ----------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **Description**               | Hardware interrupt is an interrupt generated from an external device or hardware. | Software interrupt is the interrupt that is generated by any internal system of the computer (instruction in the program). |
| **Type Of The process**       | Hardware interrupts are asynchronized events.                | Software interrupts are synchronized events.                 |
| **Effect On Program Counter** | Hardware interrupts do not increment the program counter.    | Software interrupts increase the program counter.            |
| **Cause**                     | Hardware interrupt is a kind of computer system interrupt that occur as a result of outside interference, whether that’s from the user, from peripherals, from other hardware devices or through a network. | Software interrupt is a type of interrupt that is caused either by a special instruction in the instruction set or by an exceptional condition in the processor itself. |
| **Categories**                | Maskable interrupt and Non Maskable interrupts.              | Normal interrupt Exception                                   |
| **Trigger**                   | Hardware interrupt is triggered by external hardware and is considered one of the ways to communicate with the outside peripherals, hardware. | Software interrupt is triggered by software (program instructions) and considered one of the ways to communicate with kernel or to trigger system calls, especially during error or exception handling. |
| **Priority**                  | Hardware interrupt has the lowest priority than software interrupts. | Software interrupt has the highest priority than hardware interrupt. |

### 类Unix OS: 用户空间和内核空间

在任意时刻， 一个 CPU 核心上（processor）只可能运行一个进程 。

![img](https://qph.fs.quoracdn.net/main-qimg-150cb90563a482ea7d2198964beee8fb)

##### System call

In computing, a system call (commonly abbreviated to syscall) is the programmatic way in which a computer program requests a service from the kernel of the operating system on which it is executed.This may include **hardware-related services** (for example, accessing a hard disk drive), **creation and execution of new processes**, and communication with integral kernel services such as **process scheduling**. System calls provide an essential interface between a process and the operating system.

##### Switching from User to Kernel Mode

- The user-mode program places values in registers, or creates a stack frame with arguments, to indicate what specific service it requires from the operating system.
- The user-mode program then performs the **trap** instruction (syscall).
- Immediately, the CPU switches to kernel mode, and jumps to instructions at a fixed location in memory.
- These instruction, which are part of the operating system, have memory protections so that they cannot be modified by user-mode programs, and may also be unreadable by user-mode programs.
- The instructions, known as the trap or system call handler, read the details of the requested service + arguments, and then perform this request in kernel mode.
- With the system call done, the operating system resets the mode to user-mode and returns from the system call, or there is an instruction to do both at the same time.

![Figs/intexcepsyscalls.gif](https://minnie.tuhs.org/CompArch/Lectures/Figs/intexcepsyscalls.gif)


Linux中任何一个用户进程被创建时都包含2个栈：内核栈、用户栈，并且是进程私有的，进程从用户态开始运行。当进程在执行用户自己的代码时，则称其处于用户态。即此时处理器在特权级最低的用户代码中运行。当一个任务（进程）执行系统调用而陷入内核代码中执行时，我们就称进程处于内核态。此时处理器处于特权级最高的内核代码中执行。当进程处于内核态时，执行的内核代码会使用当前进程的内核栈。

用户空间的应用程序，通过系统调用，进入内核空间。这个时候用户空间的进程要传递很多变量、参数的值给内核，内核态运行的时候也要保存用户进程的一些寄存器值、变量等。所谓的“进程上下文”，可以看作是用户进程传递给内核的这些参数以及内核要保存的那一整套的变量和寄存器值和当时的环境等。

##### Clock interrupt



### DMA

**Direct memory access** (**DMA**) is a feature of computer systems that allows certain hardware subsystems to access main system memory(random-access memory) independent of the central processing unit (CPU).

DMA can lead to cache coherency problems.

![img](https://upload.wikimedia.org/wikipedia/commons/thumb/4/49/Cache_incoherence_write.svg/559px-Cache_incoherence_write.svg.png)


### Zero Copy 

"**Zero-copy**" describes computer operations in which the CPU does not perform the task of copying data from one memory area to another. This is frequently used to save CPU cycles and memory bandwidth when transmitting a file over a network.

**Traditional data copying approach**

![Traditional data copying approach](https://developer.ibm.com/developer/default/articles/j-zerocopy/images/figure1.gif)

**Traditional context switches**

![Traditional context switches](https://developer.ibm.com/developer/default/articles/j-zerocopy/images/figure2.gif)

**Data copy with transferTo(), use zero copy approach**

![Data copy with transferTo()](https://developer.ibm.com/developer/default/articles/j-zerocopy/images/figure3.gif)

**Context switching with transferTo(), use zero copy approach**

![Context switching when using transferTo()](https://developer.ibm.com/developer/default/articles/j-zerocopy/images/figure4.gif)



The Linux kernel supports zero-copy through various system calls, such as

- sys/socket.h's sendfile, sendfile64
- splice, tee, vmsplice
- process_vm_readv, process_vm_writev
- copy_file_range
- raw sockets with packet mmap or AF_XDP

### The Internal Processor Bus
There are three internal buses associated with processors: the data bus, address bus, and control bus.

Any data that has to be manipulated must also be loaded into RAM, modified, then written back out. (see virtual memory)

### Virtual Memory

"Virtual memory" provides the programmer or the user with the perception that there is a much larger amount of RAM in the computer than is really there.

![img](https://upload.wikimedia.org/wikipedia/commons/thumb/6/6e/Virtual_memory.svg/250px-Virtual_memory.svg.png)

- 虚拟地址
- 物理地址
- 内存管理单元（Memory Management Unit, MMU）：将虚拟地址转换为物理地址，MMU需要借助存放在内存中的页表来动态翻译虚拟地址，该页表由操作系统管理。

![虚拟寻址](https://user-gold-cdn.xitu.io/2017/10/31/64ebc813fa579e80d52459ae25618925?imageView2/0/w/1280/h/960/format/webp/ignore-error/1)

### Memory-mapped file

A memory-mapped file is a segment of **virtual memory** that has been assigned a direct byte-for-byte correlation with some portion of a file or file-like resource. This resource is typically a file that is physically present on disk, but can also be a device, shared memory object, or other resource that the operating system can reference through a file descriptor. Once present, this correlation between the file and the memory space permits applications to treat the mapped portion as if it were primary memory.

The benefit of memory mapping a file is increasing I/O performance, especially when used on large files. For small files, memory-mapped files can result in a waste of slack space as memory maps are always aligned to the page size, which is mostly 4 KiB. Therefore, a 5 KiB file will allocate 8 KiB and thus 3 KiB are wasted. Accessing memory mapped files is faster than using direct read and write operations for two reasons. Firstly, a system call is orders of magnitude slower than a simple change to a program's local memory. Secondly, in most operating systems the memory region mapped actually is the kernel's page cache (file cache), meaning that no copies need to be created in user space.

The memory mapping process is handled by the virtual memory manager, which is the same subsystem responsible for dealing with the page file. Memory mapped files are loaded into memory one entire **page** at a time. The page size is selected by the operating system for maximum performance. Since page file management is one of the most critical elements of a virtual memory system, loading page sized sections of a file into physical memory is typically a very highly optimized system function.

内存映射可以绕过内核直接在用户态对文件进行IO操作。（Zero Copy）

Perhaps the most common use for a memory-mapped file is the process loader in most modern operating systems (including Microsoft Windows and Unix-like systems.)  When a process is started, the operating system uses a memory mapped file to bring the executable file, along with any loadable modules, into memory for execution. Most memory-mapping systems use a technique called demand paging, where the file is loaded into physical memory in subsets (one page each), and only when that page is actually referenced.

Another common use for memory-mapped files is to share memory between multiple processes. In modern protected mode operating systems, processes are generally not permitted to access memory space that is allocated for use by another process. (A program's attempt to do so causes invalid page faults or segmentation violations.) There are a number of techniques available to safely share memory, and memory-mapped file I/O is one of the most popular. Two or more applications can simultaneously map a single physical file into memory and access this memory. 

##### mmap
In computing, mmap(2) is a POSIX-compliant Unix system call that maps files or devices into memory.

The Java programming language provides classes and methods to access memory mapped files, such as FileChannel.

### IO multiplexing

One basic concept of Linux (actually Unix) is the rule that everything in Unix/Linux is a file. Each process has a table of file descriptors that point to files, sockets, devices and other operating system objects.

In computing, I/O multiplexing can also be used to refer to the concept of processing multiple input/output events from a single event loop, with system calls like poll and select (Unix).

There are 3 options you can use in Linux:

- select 
- poll
- epoll

All the above methods serve the same idea, create a set of file descriptors, tell the kernel what would you like to do with each file descriptor (read, write, ..) and use one thread to block on one function call until at least one file descriptor requested operation available.

##### select  system call

```c++
int select(int nfds, fd_set *readfds, fd_set *writefds, fd_set *exceptfds, struct timeval *timeout);
```

A call to select( ) will block until the given file descriptors are ready to perform I/O, or until an optionally specified timeout has elapsed.

The watched file descriptors are broken into three sets

- File descriptors listed in the readfds set are watched to see if data is available for reading.
- File descriptors listed in the writefds set are watched to see if a write operation will complete without blocking.
- File descriptors in the exceptfds set are watched to see if an exception has occurred, or if out-of-band data is available (these states apply only to sockets).

On successful return, each set is modified such that it contains only the file descriptors that are ready for I/O of the type delineated by that set.

Select – summary:

- We need to build each set before each call
- The function check any bit up to the higher number – O(n)
- We need to iterate over the file descriptors to check if it exists on the set returned from select
- The main advantage of select is the fact that it is very portable – every unix like OS has it

##### poll system call

```c++
int poll (struct pollfd *fds, unsigned int nfds, int timeout);
```

The structure pollfd has a different fields for the events and the returning events so we don’t need to build it each time:

```c++
struct pollfd {
      int fd;
      short events; 
      short revents;
};
```

Poll vs Select

- poll() does not require that the user calculate the value of the highest- numbered file descriptor +1
- poll() is more efficient for large-valued file descriptors. Imagine watching a single file descriptor with the value 900 via select()—the kernel would have to check each bit of each passed-in set, up to the 900th bit.
- select()’s file descriptor sets are statically sized.
- With select(), the file descriptor sets are reconstructed on return, so each subsequent call must reinitialize them. The poll() system call separates the input (events field) from the output (revents field), allowing the array to be reused without change.
- The timeout parameter to select() is undefined on return. Portable code needs to reinitialize it. This is not an issue with pselect().
- select() is more portable, as some Unix systems do not support poll()

##### epoll system call

While working with select and poll we manage everything on user space and we send the sets on each call to wait. To add another socket we need to add it to the set and call select/poll again.

Epoll system calls help us to create and manage the context in the kernel. We divide the task to 3 steps:

- create a context in the kernel using *epoll_create*
- add and remove file descriptors to/from the context using *epoll_ctl*
- wait for events in the context using *epoll_wait*

Epoll vs Select/Poll

- We can add and remove file descriptor while waiting
- *epoll_wait* returns only the objects with ready file descriptors
- epoll has better performance – O(1) instead of O(n)
- epoll can behave as **level triggered** or **edge triggered** (see man page)
- epoll is Linux specific so non portable.

##### Level Triggered  and Edge Triggered
A descriptor is considered ready if a process can perform an I/O operation on the descriptor without blocking. For a descriptor to be considered “ready”, it doesn’t matter if the operation would actually transfer any data — all that matters is that the I/O operation can be performed without blocking.

A descriptor changes into a **ready** state when an I/O *event* happens, such as the arrival of new input or the completion of a socket connection or when space is available on a previously full socket send buffer after TCP transmits queued data to the socket peer.

There are two ways to find out about the readiness status of a descriptor — edge triggered and level triggered.

Epoll provides both edge-triggered and level-triggered modes. In edge-triggered mode, a call to *epoll_wait* will return only when a new event is enqueued with the epoll object, while in level-triggered mode, *epoll_wait* will return as long as the condition holds.

For instance, if a pipe registered with epoll has received data, a call to *epoll_wait* will return, signaling the presence of data to be read. Suppose, the reader only consumed part of data from the buffer. In level-triggered mode, further calls to *epoll_wait* will return immediately, as long as the pipe's buffer contains data to be read. In edge-triggered mode, however, *epoll_wait* will return only once new data is written to the pipe (descriptor change into ready state).

Redis 采用 level triggered 的方式，且不兼容 edge triggered. 引用开发者相关描述：
However, we would need to be aware of whether we are in ET mode or not. Otherwise we risk starving other I/O (and CPU time) if there is a lot of data on the socket.[<sup>1</sup>](https://github.com/redis/hiredis/issues/615) （ET模式下只有新事件会触发进程的IO操作，可能会导致socket中缓存数据量过大）。



# References

\[1\]:[Redis Commands](https://redis.io/commands) <br />
\[2\]:[Memcached vs Redis](https://www.linkedin.com/pulse/memcached-vs-redis-which-one-pick-ranjeet-vimal)<br />
\[3\]:[Redis命令参考](http://doc.redisfans.com/)<br />
\[4\]:[Try Redis](http://try.redis.io/)<br />
\[5\]:[IO模型](https://www.jianshu.com/p/f00ad612153b)<br />
\[6\]:[IO概念区分](https://www.zhihu.com/question/19732473)<br />
\[7\]:[Hardware Interrupt VS Software Interrupt ](https://vivadifferences.com/7-difference-between-hardware-interrupt-and-software-interrupt/)<br />
\[8\]:[User mode and Kernel mode](https://minnie.tuhs.org/CompArch/Lectures/week05.html)<br />
\[9\]:[Operating System](https://en.wikipedia.org/wiki/Operating_system)<br />
\[10\]:[IO](https://juejin.im/post/6844904153735512072)<br />
\[11\]:[Direct Memory Access](https://en.wikipedia.org/wiki/Direct_memory_access)
\[12\]:[The Internal Processor Bus](https://www.microcontrollertips.com/internal-processor-bus-data-address-control-bus-faq/)
\[13\]:[Quora](https://www.quora.com/Why-wont-the-computer-system-use-the-hard-disk-memory-as-additional-RAM)
\[14\]:[Zero Copy](https://developer.ibm.com/articles/j-zerocopy/)
\[15\]:[Virtual Memory](https://en.wikipedia.org/wiki/Virtual_memory)
\[16\]:[虚拟内存](https://zhuanlan.zhihu.com/p/82746153)
\[17\]:[虚拟内存](https://juejin.im/post/6844903507594575886)
\[18\]:[Memory-mapped file](https://en.wikipedia.org/wiki/Memory-mapped_file)
\[19\]:[mmap](https://en.wikipedia.org/wiki/Mmap)
\[20\]:[select,poll,epoll](https://devarea.com/linux-io-multiplexing-select-vs-poll-vs-epoll/#.X4aWjmj7SUl)
\[21\]:[epoll](https://medium.com/@copyconstruct/the-method-to-epolls-madness-d9d2d6378642)
\[22\]:[Non-blocking IO](https://medium.com/@copyconstruct/nonblocking-i-o-99948ad7c957)
\[23\]:[epoll](https://en.wikipedia.org/wiki/Epoll)
\[24\]:[Redis](https://xie.infoq.cn/article/3b91bbbcbb68bd049347fd541)
\[25\]:[Redis Hotspot key and big Key](https://zhuanlan.zhihu.com/p/52393940)
\[26\]:[Redis Hotspot Key](https://www.alibabacloud.com/blog/redis-hotspot-key-discovery-and-common-solutions_594446?spm=a2c41.12559851.0.0)
\[27\]:[Redis过期策略和内存淘汰策略](https://juejin.im/post/6844903953092575246)
\[28\]:[Redis过期策略和内存淘汰策略](https://redis.io/topics/lru-cache)

