Kafka: A distributed streaming platform.

# Concepts

### Apache Kafka® is an distributed event streaming platform.

Kafka combines three key capabilities so you can implement your use cases for event streaming end-to-end with a single battle-tested solution:

1. To **publish** (write) and **subscribe to** (read) streams of events, including continuous import/export of your data from other systems.
2. To **store** streams of events durably and reliably for as long as you want.
3. To **process** streams of events as they occur or retrospectively.

And all this functionality is provided in a distributed, highly scalable, elastic, fault-tolerant, and secure manner. Kafka can be deployed on bare-metal hardware, virtual machines, and containers, and on-premises as well as in the cloud. You can choose between self-managing your Kafka environments and using fully managed services offered by a variety of vendors.

Kafka is a distributed system consisting of **servers** and **clients** that communicate via a high-performance **TCP network protocol**. 

**Servers**: Kafka is run as a cluster of one or more servers that can span multiple datacenters or cloud regions. Some of these servers form the storage layer, called the **brokers**. Other servers run Kafka Connect to continuously import and export data as event streams to integrate Kafka with your existing systems such as relational databases as well as other Kafka clusters. To let you implement mission-critical use cases, a Kafka cluster is highly scalable and fault-tolerant: if any of its servers fails, the other servers will take over their work to ensure continuous operations without any data loss.

**Clients**: They allow you to write distributed applications and microservices that read, write, and process streams of events in parallel, at scale, and in a fault-tolerant manner even in the case of network problems or machine failures. 

An **event** records the fact that "something happened" in the world or in your business. It is also called record or message in the documentation. When you read or write data to Kafka, you do this in the form of events. Conceptually, an event has a key, value, timestamp, and optional metadata headers.

**Producers** are those client applications that publish (write) events to Kafka, and **consumers** are those that subscribe to (read and process) these events. In Kafka, producers and consumers are fully decoupled and agnostic of each other, which is a key design element to achieve the high scalability that Kafka is known for.

Events are organized and durably stored in **topics**. Very simplified, **a topic is similar to a folder in a filesystem, and the events are the files in that folder**. Topics in Kafka are always multi-producer and multi-subscriber: a topic can have zero, one, or many producers that write events to it, as well as zero, one, or many consumers that subscribe to these events. Events in a topic can be read as often as needed—unlike traditional messaging systems, events are not deleted after consumption. Instead, you define for how long Kafka should retain your events through a per-topic configuration setting, after which old events will be discarded. Kafka's performance is effectively constant with respect to data size, so storing data for a long time is perfectly fine.

Topics are **partitioned**, meaning a topic is spread over a number of "buckets" located on different Kafka brokers. When a new event is published to a topic, it is actually appended to one of the topic's partitions. Events with the same event key (e.g., a customer or vehicle ID) are written to the same partition, and Kafka guarantees that any consumer of a given topic-partition will always read that partition's events in exactly the same order as they were written.

![img](E:\GitRepository\test\image\streams-and-tables-p1_p4.png) 

*Events with the same key (denoted by their color in the figure) are written to the same partition.* 

To make your data fault-tolerant and highly-available, every topic can be **replicated**, even across geo-regions or datacenters, so that there are always multiple brokers that have a copy of the data just in case things go wrong, you want to do maintenance on the brokers, and so on. A common production setting is a replication factor of 3, i.e., there will always be three copies of your data. **This replication is performed at the level of topic-partitions.**

# Quick Start 

```
# unzip kafka
$ tar -xzf kafka_2.13-2.6.0.tgz
$ cd kafka_2.13-2.6.0

# Start the ZooKeeper service
# Note: Soon, ZooKeeper will no longer be required by Apache Kafka.
$ bin/zookeeper-server-start.sh config/zookeeper.properties

# Start the Kafka broker service
$ bin/kafka-server-start.sh config/server.properties

# create a topic to store your events
$ bin/kafka-topics.sh --create --topic quickstart-events --bootstrap-server localhost:9092

# Run the console producer client to write a few events into your topic. By default, each line you enter will result in a separate event being written to the topic.
$ bin/kafka-console-producer.sh --topic quickstart-events --bootstrap-server localhost:9092
This is my first event
This is my second event

# Run the console consumer client to read the events you just created.
$ bin/kafka-console-consumer.sh --topic quickstart-events --from-beginning --bootstrap-server localhost:9092

# Stop the producer and consumer clients with Ctrl-C.
# Stop the Kafka broker with Ctrl-C.
# Lastly, stop the ZooKeeper server with Ctrl-C

# Delete any data of your local Kafka environment including any events you have created along the way, run the command
$ rm -rf /tmp/kafka-logs /tmp/zookeeper

```



# Kafka APIs

### Producer API

The Producer API allows applications to send streams of data to topics in the Kafka cluster.

```xml
<dependency>
	<groupId>org.apache.kafka</groupId>
	<artifactId>kafka-clients</artifactId>
	<version>2.6.0</version>
</dependency>
```

### Consumer API

The Consumer API allows applications to read streams of data from topics in the Kafka cluster.

```xml
<dependency>
	<groupId>org.apache.kafka</groupId>
	<artifactId>kafka-clients</artifactId>
	<version>2.6.0</version>
</dependency>
```



### Kafka Streams API

The Streams API allows transforming streams of data from input topics to output topics.

```xml
<dependency>
	<groupId>org.apache.kafka</groupId>
	<artifactId>kafka-streams</artifactId>
	<version>2.6.0</version>
</dependency>
```



### Kafka Connect API

The Connect API allows implementing connectors that continually pull from some source data system into Kafka or push from Kafka into some sink data system.

### Admin API

The Admin API supports managing and inspecting topics, brokers, ACLs (Access Control List), and other Kafka objects.

```xml
<dependency>
	<groupId>org.apache.kafka</groupId>
	<artifactId>kafka-clients</artifactId>
	<version>2.6.0</version>
</dependency>
```

# Configuration

### broken configuration

- `broker.id`: The broker id for this server. If unset, a unique broker id will be generated.To avoid conflicts between zookeeper generated broker id's and user configured broker id's, generated broker ids start from reserved.broker.max.id + 1.
- `log.dirs`: The directories in which the log data is kept. If not set, the value in log.dir is used.
- `log.dir`:  The directory in which the log data is kept (supplemental for log.dirs property).
- `zookeeper.connect`
- `log.flush.interval.messages`: The number of messages accumulated on a log partition before messages are flushed to disk.
- `log.flush.interval.ms`: The maximum time in ms that a message in any topic is kept in memory before flushed to disk. If not set, the value in log.flush.scheduler.interval.ms is used.
- `log.flush.scheduler.interval.ms`: The frequency in ms that the log flusher checks whether any log needs to be flushed to disk.
- `log.retention.bytes`: The maximum size of the log before deleting it.
- `log.retention.ms`
- `log.retention.minutes`
- `log.retention.hours`
- `log.segment.bytes`: The maximum size of a single log file.
- `log.segment.delete.delay.ms`: The amount of time to wait before deleting a file from the filesystem.
- `advertised.listeners`: Listeners to publish to ZooKeeper for clients to use, if different than the listeners config property.
- `auto.create.topics.enable`: Enable auto creation of topic on the server.
- `background.threads`: The number of threads to use for various background processing tasks.
- `compression.type`: Specify the final compression type for a given topic. This configuration accepts the standard compression codecs ('gzip', 'snappy', 'lz4', 'zstd'). It additionally accepts 'uncompressed' which is equivalent to no compression; and 'producer' which means retain the original compression codec set by the producer.
- `delete.topic.enable`: Enables delete topic. Delete topic through the admin tool will have no effect if this config is turned off.

### Topic-Level Configs
Configurations pertinent to topics have both a server default as well an optional per-topic override. If no per-topic configuration is given the server default is used.

The override can be set at topic creation time by giving one or more --config options. 
```
> bin/kafka-topics.sh --bootstrap-server localhost:9092 --create --topic my-topic --partitions 1 \
      --replication-factor 1 --config max.message.bytes=64000 --config flush.messages=1
```

Overrides can also be changed or set later using the alter configs command.

```
> bin/kafka-configs.sh --bootstrap-server localhost:9092 --entity-type topics --entity-name my-topic
      --alter --add-config max.message.bytes=128000
```

To check overrides set on the topic you can do

```
> bin/kafka-configs.sh --bootstrap-server localhost:9092 --entity-type topics --entity-name my-topic --describe
```

To remove an override you can do

```
> bin/kafka-configs.sh --bootstrap-server localhost:9092  --entity-type topics --entity-name my-topic
      --alter --delete-config max.message.bytes
```

- `cleanup.policy`
- `compression.type`
- `delete.retention.ms`
- `file.delete.delay.ms`
- `segment.bytes`

### Producer Configs

- `key.serializer`: Serializer class for key that implements the `org.apache.kafka.common.serialization.Serializer` interface.
- `value.serializer`:  Serializer class for value that implements the `org.apache.kafka.common.serialization.Serializer` interface.
- `acks`: The number of acknowledgments the producer requires the leader to have received before considering a request complete. This controls the durability of records that are sent. The following settings are allowed: 
  - `acks=0` If set to zero then the producer will not wait for any acknowledgment from the server at all. The record will be immediately added to the socket buffer and considered sent. No guarantee can be made that the server has received the record in this case, and the `retries` configuration will not take effect (as the client won't generally know of any failures). The offset given back for each record will always be set to -1.
  - `acks=1` This will mean the leader will write the record to its local log but will respond without awaiting full acknowledgement from all followers. In this case should the leader fail immediately after acknowledging the record but before the followers have replicated it then the record will be lost.
  - `acks=all` This means the leader will wait for the full set of in-sync replicas to acknowledge the record. This guarantees that the record will not be lost as long as at least one in-sync replica remains alive. This is the strongest available guarantee. This is equivalent to the acks=-1 setting.
- `bootstrap.servers`: A list of host/port pairs to use for establishing the initial connection to the Kafka cluster. This list should be in the form `host1:port1,host2:port2,...`.
- `buffer.memory`: The total bytes of memory the producer can use to buffer records waiting to be sent to the server. If records are sent faster than they can be delivered to the server the producer will block for max.block.ms after which it will throw an exception.
- `compression.type`: The compression type for all data generated by the producer.
- `retries`: Setting a value greater than zero will cause the client to resend any record whose send fails with a potentially transient error. Note that this retry is no different than if the client resent the record upon receiving the error. Allowing retries without setting `max.in.flight.requests.per.connection` to 1 will potentially change the ordering of records because if two batches are sent to a single partition, and the first fails and is retried but the second succeeds, then the records in the second batch may appear first. Note additionally that produce requests will be failed before the number of retries has been exhausted if the timeout configured by `delivery.timeout.ms` expires first before successful acknowledgement. Users should generally prefer to leave this config unset and instead use `delivery.timeout.ms` to control retry behavior.
- `ssl.key.password`: The password of the private key in the key store file.
- `ssl.keystore.location`: The location of the key store file.
- `ssl.keystore.password`: The store password for the key store file.
- `batch.size`: The producer will attempt to batch records together into fewer requests whenever multiple records are being sent to the same partition. This helps performance on both the client and the server. This configuration controls the default batch size in bytes. No attempt will be made to batch records larger than this size.
- `client.dns.lookup`: Controls how the client uses DNS lookups.
- `client.id`
- `connections.max.idle.ms`: Close idle connections after the number of milliseconds specified by this config.
- `delivery.timeout.ms`
- `max.request.size`
- `partitioner.class`: Partitioner class that implements the `org.apache.kafka.clients.producer.Partitioner` interface.
- `receive.buffer.bytes`
- `request.timeout.ms`
- `send.buffer.bytes`
- `interceptor.classes`: A list of classes to use as interceptors. Implementing the `org.apache.kafka.clients.producer.ProducerInterceptor` interface allows you to intercept (and possibly mutate) the records received by the producer before they are published to the Kafka cluster. By default, there are no interceptors.

### Consumer Configs
- `key.deserializer`: Deserializer class for key that implements the `org.apache.kafka.common.serialization.Deserializer` interface.
- `value.deserializer`: Deserializer class for value that implements the `org.apache.kafka.common.serialization.Deserializer` interface.
- `bootstrap.servers`
- `fetch.min.bytes`: The minimum amount of data the server should return for a fetch request. If insufficient data is available the request will wait for that much data to accumulate before answering the request. The default setting of 1 byte means that fetch requests are answered as soon as a single byte of data is available or the fetch request times out waiting for data to arrive.
- `group.id`: A unique string that identifies the consumer group this consumer belongs to. This property is required if the consumer uses either the group management functionality by using `subscribe(topic)` or the Kafka-based offset management strategy.
- `heartbeat.interval.ms`
- `max.partition.fetch.bytes`
- `session.timeout.ms`
- `ssl.key.password`
- `ssl.keystore.location`
- `ssl.keystore.password`
- `ssl.truststore.location`
- `ssl.truststore.password`
- `allow.auto.create.topics`: Allow automatic topic creation on the broker when subscribing to or assigning a topic.
- `auto.offset.reset`: What to do when there is no initial offset in Kafka or if the current offset does not exist any more on the server (e.g. because that data has been deleted):
  - earliest: automatically reset the offset to the earliest offset
  - latest: automatically reset the offset to the latest offset
  - none: throw exception to the consumer if no previous offset is found for the consumer's group
  - anything else: throw exception to the consumer.
- `client.dns.lookup`
- `connections.max.idle.ms`
- `default.api.timeout.ms`
- `enable.auto.commit`: If true the consumer's offset will be periodically committed in the background.

### Connect Configs
- `config.storage.topic`
- `group.id`
- `key.converter`
- `offset.storage.topic`
- `status.storage.topic`
- `value.converter`
- `bootstrap.servers`
- `connect.protocol`
- `header.converter`

### Streams Configs
- `application.id`
- `bootstrap.servers`
- `replication.factor`
- `state.dir`
- `client.id`

### Admin Configs
- `bootstrap.servers`
- `ssl.key.password`
- `ssl.keystore.location`
- `ssl.keystore.password`
- `ssl.truststore.location`
- `ssl.truststore.password`

# Design
### Persistence 
##### Don't fear the filesystem!

**Kafka relies heavily on the filesystem for storing and caching messages.** There is a general perception that "disks are slow" which makes people skeptical that a persistent structure can offer competitive performance. In fact disks are both much slower and much faster than people expect depending on how they are used; and a properly designed disk structure can often be as fast as the network.  A modern operating system provides **read-ahead** and **write-behind** techniques that prefetch data in large block multiples and group smaller logical writes into large physical writes. **Sequential disk access can in some cases be faster than random memory access!**

To compensate for this performance divergence, modern operating systems have become increasingly aggressive in their use of main memory for disk caching. A modern OS will happily divert *all* free memory to disk caching with little performance penalty when the memory is reclaimed. All disk reads and writes will go through this unified cache. This feature cannot easily be turned off without using direct I/O, so even if a process maintains an in-process cache of the data, this data will likely be duplicated in OS page cache, effectively storing everything twice.

Furthermore, we are **building on top of the JVM**, and anyone who has spent any time with Java memory usage knows two things:

1. The memory overhead of objects is very high, often doubling the size of the data stored (or worse).
2. Java garbage collection becomes increasingly fiddly and slow as the in-heap data increases.

As a result of these factors using the filesystem and relying on page cache is superior to maintaining an in-memory cache or other structure—we at least double the available cache by having automatic access to all free memory, and likely double again by storing a compact byte structure rather than individual objects.

This suggests a design which is very simple: rather than maintain as much as possible in-memory and flush it all out to the filesystem in a panic when we run out of space, we invert that. All data is immediately written to a persistent log on the filesystem without necessarily flushing to disk. In effect this just means that it is transferred into the kernel's page cache.

##### Constant Time Suffices
The persistent data structure used in messaging systems are often a per-consumer queue with an associated **BTree** or other general-purpose random access data structures to maintain metadata about messages.

### Efficiency

Once poor disk access patterns have been eliminated, there are two common causes of inefficiency in this type of system: too many small I/O operations, and excessive byte copying.

The small I/O problem happens both between the client and the server and in the server's own persistent operations. To avoid this, our protocol is built around a "message set" abstraction that naturally groups messages together. This allows network requests to group messages together and amortize the overhead of the network roundtrip rather than sending a single message at a time. The server in turn appends chunks of messages to its log in one go, and the consumer fetches large linear chunks at a time.

The other inefficiency is in byte copying. At low message rates this is not an issue, but under load the impact is significant. To avoid this we employ a standardized binary message format that is shared by the producer, the broker, and the consumer (so data chunks can be transferred without modification between them). 

The message log maintained by the broker is itself just a directory of files, each populated by a sequence of message sets that have been written to disk in the same format used by the producer and consumer. Maintaining this common format allows optimization of the most important operation: network transfer of persistent log chunks. Modern unix operating systems offer a highly optimized code path for transferring data out of pagecache to a socket; in Linux this is done with the **sendfile** system call.

This combination of **pagecache** and **sendfile**(zero-copy) means that on a Kafka cluster where the consumers are mostly caught up you will see no read activity on the disks whatsoever as they will be serving data entirely from cache.

##### End-to-end Batch Compression
In some cases the bottleneck is actually not CPU or disk but network bandwidth. Efficient compression requires compressing multiple messages together rather than compressing each message individually.

Kafka supports this with an efficient batching format. A batch of messages can be clumped together compressed and sent to the server in this form. This batch of messages will be written in compressed form and will remain compressed in the log and will only be decompressed by the consumer.

Kafka supports GZIP, Snappy, LZ4 and ZStandard compression protocols.

### The Producer

##### Load balancing

The producer sends data directly to the broker that is the leader for the partition without any intervening routing tier. To help the producer do this all Kafka nodes can answer a request for metadata about which servers are alive and where the leaders for the partitions of a topic are at any given time to allow the producer to appropriately direct its requests.

The client controls which partition it publishes messages to. This can be done at random, implementing a kind of random load balancing, or it can be done by some semantic partitioning function.

##### Asynchronous send

Batching is one of the big drivers of efficiency, and to enable batching the Kafka producer will attempt to accumulate data in memory and to send out larger batches in a single request. This buffering is configurable and gives a mechanism to trade off a small amount of additional latency for better throughput.

### The Consumer 

The consumer specifies its offset in the log with each request and receives back a chunk of log beginning from that position. The consumer thus has significant control over this position and can rewind it to re-consume data if need be.

##### Push vs. pull

An initial question we considered is whether consumers should pull data from brokers or brokers should push data to the consumer. In this respect Kafka follows a more traditional design, shared by most messaging systems, where **data is pushed to the broker from the producer and pulled from the broker by the consumer.**

The deficiency of a naive pull-based system is that if the broker has no data the consumer may end up polling in a tight loop, effectively busy-waiting for data to arrive. To avoid this we have parameters in our pull request that allow the consumer request to block in a "long poll" waiting until data arrives (and optionally waiting until a given number of bytes is available to ensure large transfer sizes).

##### Consumer Position

Keeping track of *what* has been consumed is, surprisingly, one of the key performance points of a messaging system.

**Kafka's topic is divided into a set of totally ordered partitions, each of which is consumed by exactly one consumer within each subscribing consumer group at any given time.** This means that the position of a consumer in each partition is just a single integer, the offset of the next message to consume. This makes the state about what has been consumed very small, just one number for each partition. This state can be periodically checkpointed. This makes the equivalent of message acknowledgements very cheap.

There is a side benefit of this decision. A consumer can deliberately *rewind* back to an old offset and re-consume data. This violates the common contract of a queue, but turns out to be an essential feature for many consumers. For example, if the consumer code has a bug and is discovered after some messages are consumed, the consumer can re-consume those messages once the bug is fixed.

##### Offline Data Load







# Reference 

[Kafka 官网](http://kafka.apache.org/documentation/)
[Kafka 系列](https://xie.infoq.cn/article/c866a4560967dc6bb5e0cf809)