
> java同步机制：
 - synchronized关键字： 提供一种独占的加锁方式
 - volatile 
 - 显示锁 (Explicit Lock)
 - 原子变量

> 如果多个线程访问同一个可变的状态变量时没有使用合适的同步，那么程序就会出现错误。可以有三种方式修复这个问题：
  - 不在线程间共享该状态变量；
  - 将状态变量修改为不可变的变量；
  - 在访问状态变量时使用同步；
  
> 编写并发代码的原则：

 首先使代码正确运行，然后再提高代码的速度。即使如此，最好也只是当性能测试结果和应用需求告诉你必须提高性能，以及测量结果表明这种优化在实际环境中确实能带来性能的提升时，才进行优化。
 
> 竞态条件(Race Condition)：多个线程由于不恰当的执行时序而出现不正确的结果

大多数竞态条件的本质：基于一种可能失效的观察结果来做出判断或者执行某个计算。
( **数据竞争：如果在访问共享的非final类型的域时没有采用同步来进行协同，那么就会出现数据竞争。**)

> 通常在简单性和性能之间存在相互制约因素。当实现某个同步策略时，一定不要盲目地为了性能而牺牲简单性(这可能会破坏安全性)。

> 当执行时间较长的计算或者可能无法快速完成的操作时(例如，网络I/O或控制台I/O),一定不要持有锁。

> 重排序：只要在某个线程中无法检测到重排序的情况(即使在其他线程中可以明显地看到该线程中的重排序)，那么就无法确保线程中的操作将按照程序中指定的顺序来执行。

在没有同步的情况下，编译器、处理器以及运行时等都可能对操作的执行顺序进行一些意想不到的调整。在缺乏足够同步的多线程程序中，要想对内存操作的执行顺序进行判断，几乎无法得出正确的结论。

> java内存模型要求，变量的读取操作和写入操作都必须是原子操作，但对于非volatile类型 的double和long变量，JVM允许将64位的读操作和写操作分解成两个32位的操作。当读取一个非volatile类型的long变量时，如果该变量的读操作和写操作在不同的线程中执行，那么很可能会读取到某个值的高32位和另一个值的低32位。

> 加锁的含义不仅仅局限于互斥行为，还包括内存可见性，为了确保所有线程都能看到共享变量的最新值，所有执行读操作或者写操作都必须在同一个锁上同步。

> volatile 变量: 在访问volatile变量时不会执行加锁操作，因此也就不会执行线程阻塞，所以volatile变量是比synchronized关键字更轻量级的同步机制；volatile变量会限制一些重排序操作，volatile变量不会被缓存在寄存器或者对其他处理器不可见的地方，因此在读取volatile类型的变量时总会返回最新写入的值。

volatile变量的正确使用方式： 确保它们自身状态的可见性，确保它们所引用对象的状态的可见性，以及标识一些重要的程序生命周期事件的发生(例如，初始化或关闭)。
<br />
加锁机制既可以确保可见性又可以确保原子性，而volatile变量只能确保可见性。
<br />
当且仅当满足以下条件时，才应该使用volatile变量：
 - 对变量的写入操作不依赖变量的当前值，或者能确保只有单个线程更新变量的值；
 - 该变量不会与其他状态变量一起纳入不变性条件中；
 - 在访问变量时不需要加锁；

<br />
volatile关键字保证可见性和有序性，但不保证原子性。

> 发布(publish)与逸出(escape)： 发布一个对象是指使对象能在当前作用域之外的代码中使用。当某个不应该发布的对象被发布时，这种情况被称为逸出。
``` java
	public static Set<Secret> knownSecrets;
	
	public void initialize() {
		knownSecrets = new HashSet<Secret>();
	}
```
> 线程封闭： 当访问共享的可变数据时，通常需要同步。一种避免使用同步的方式就是不共享数据。如果仅在单线程内访问数据，就不需要同步。

- Ad-hoc 线程封闭： 维护线程封闭性的职责完全由程序实现来承担。(脆弱，少用)
- 栈封闭：只能通过局部变量才能访问对象。java语言的语义确保了基本类型的局部变量始终封闭在线程内；在维持对象引用的栈封闭性时需要额外工作确保被引用的对象不会逸出。
- ThreadLocal类：ThreadLocal对象通常用于防止对可变的单实例变量或全局变量进行共享。当某个频繁执行的操作需要一个临时对象，例如一个缓冲区，而同时又希望避免在每次执行时都重新分配该临时对象，就可以使用该技术。(实现上ThreadLocal中存储值的对象ThreadLocalMap保存在相应线程的Thread对象中，当线程终止后，这些值会作为垃圾回收)。
``` java
 private static ThreadLocal<Connection> connectionHolder =
   new ThreadLocal<Connection>(){
       public Connection initialValue(){ // 某个线程初次调用ThreadLocal.get(),就会调用获取初始值
           return DriverManager.getConnection(DB_URL);
       }
   };
```
> 不变性： 不可变对象(immutable object)一定是线程安全的。

当满足以下条件时，对象才是不可变的：
 - 对象创建以后其状态就不能修改；
 - 对象的所有域都是final类型(从技术上来看，不可变对象并不需要将其所有的域都声明为final类型，如String的hash域)；
 - 对象是正确创建的(在对象的创建时期，this 没有逸出)；
 ```java
     public int hashCode() { // hash的计算推迟到第一次调用hashCode(),基于final域value,每次计算结果都相同
        int h = hash; 
        if (h == 0 && value.length > 0) {
            char val[] = value;
            for (int i = 0; i < value.length; i++) {
                h = 31 * h + val[i];
            }
            hash = h;
        }
        return h;
    }
 ```

> final 域：final类型的域是不能修改的(但如果final域所引用的对象是可变的，那么这些被引用的对象是可以修改的)。在java内存模型中，final域有着特殊的语义。final域能确保初始化过程的安全性，从而可以不受限制的访问不可变对象，并在共享这些对象时无需同步。

**"除非需要更高的可见性，否则应将所有的域都声明为私有域"是一个良好的编程习惯；"除非需要某个域是可变的,否则应将其声明为final域"也是一个良好的编程习惯。**

> 在并发程序中使用和共享对象时，实用的一些策略：
 - 线程封闭： 线程封闭的对象只能由一个线程拥有，对象被封闭在该线程中，并且只能由该线程修改；
 - 只读共享： 在没有额外的同步情况下，共享的只读对象可以由多个线程并发访问，但任何线程都不能修改它。共享的只读对象包括不可变对象和事实不可变对象(Effectively Immutable Object, 对象从技术上来看是可变的，但其状态在发布后不会再改变)。
 - 线程安全共享： 线程安全的对象在其内部实现同步，因此多个线程可以通过对象的公有接口来进行访问而不需要进一步的同步；
 - 保护对象： 被保护的对象只能通过持有特定的锁访问。保护对象包括封装在其他线程安全对象中的对象，以及已发布的并且由某个特定锁保护的对象。

------
> 同步容器类：Vector 、Hashtable 、 Collections.synchronizedXxx() ， 实现线程安全的方式是将状态封装起来，并对每个公有方法都进行同步，使得每次只有一个线程能访问容器的状态。同步容器将所有对容器状态的访问都串行化，以实现它们的线程安全性。这种方法的代价是严重降低并发性，当多个线程竞争容器的锁时，吞吐量将严重降低。

同步容器类都是线程安全的，但是在某些情况下可能需要额外的客户端加锁来保护符合操作。常见的符合操作：
- 迭代
- 跳转(根据指定顺序找到当前元素的下一个元素)
- 条件运算

在同步容器类中，这些复合操作在没有客户端加锁的情况下仍然是线程安全的，但当其他线程并发地修改容器时，它们可能会表现出意料之外的行为。

> 迭代器(Iterator) 和 ConcurrentModificationException: 当发现容器在迭代过程中被修改，就会抛出一个ConcurrentModificationException (fail-fast机制)；实现上是将计数器的变化和容器关联，如果迭代期间计数器被修改，则抛出异常。(**在单线程代码中也可能抛出ConcurrentModificationException异常，当对象直接从容器中删除而不是通过Iterator.remove()来删除时就会抛出该异常。<remove()方法会修改exceptedModCount的值>**)

迭代过程中避免出现ConcurrentModificationException:
- 对容器加锁
- 克隆容器，在副本上进行迭代

容器的某些方法会间接地执行迭代操作，如hashCode(),equals()等，这些同样可能会抛出ConcurrentModificationException;

-------
> 并发容器： ConcurrentHashMap (替代同步且基于散列的Map), ConcurrentSkipListMap (替代同步的SortedMap), ConcurrentSkipListSet (替代同步的SortedSet), CopyOnWriteArrayList (在遍历操作为主要操作的情况下代替同步的List), ConcurrentLinkedQueue (FIFO队列),BlockingQueue (阻塞队列，"生产-消费者"模式)<PriorityQueue，优先队列，不是并发的>

- ConcurrentHashMap : jdk 7 : segment 实现，对整个Map进行计算的方法语义进行弱化，如size返回的结果可能已经过期，实际上只是个估计值；<br /> jdk 8 : CAS，synchronized 实现


 [为并发而生的 ConcurrentHashMap（Java 8）](https://www.jianshu.com/p/e99e3fcface4)
  <br />
 [为什么ConcurrentHashMap的读操作不需要加锁？](https://juejin.im/entry/5b98b89bf265da0abd35034c)
 
 并发容器提供的迭代器不会抛出 ConcurrentModificationException ,因此不需要在迭代过程中对容器加锁。ConcurrentHashMap 返回的迭代器具有**弱一致性** (Weaklly Consistent)，而并非"fail-fast"。弱一致性的迭代器可以容忍并发的修改，当创建迭代器时会遍历已有的元素，并可以(但不保证)在迭代器被构造后将修改操作反映给容器。
 <br />

- CopyOnWriteArrayList : 每次修改容器都会复制底层数组(并且使用 ReentrantLock )，所以仅当迭代操作远远多于修改操作时才应该使用。容器的迭代器保留一个指向底层数组的引用，由于底层数组不会被改变，所以对其进行同步只需确保数组内容的可见性。该容器的迭代器不会抛出 ConcurrentModificationException 。

- BlockingQueue 和 producer-consumer模式

```java
/* Inserts the specified element into this queue, waiting if necessary for space to become available. */
    void put(E e) throws InterruptedException;
    
/* Retrieves and removes the head of this queue, waiting if necessary until an element becomes available. */    
    E take() throws InterruptedException;
```

| Implements | |
| - | - |
| ArrayBlockingQueue | FIFO，有界 |
| LinkedBlockingQueue | FIFO，有界或无界 |
| PriorityBlockingQueue | 有界，按优先级排序，自然序:Comparable 或 比较器：Comparator |
| SynchronousQueue | 同步队列，不为队列中的元素维护存储空间;它维护一组线程，这些线程在等待把元素加入或移出队列; 不是一个真正的队列，而是一种在线程之间进行移交的机制，Executors.newCachedThreadPool()使用了这种队列 |

队列可以是有界的，也可以是无界的，无界队列永远不会充满，因此无界队列上的 put 永远不会阻塞(通常这种无界不是真的无界，而是容量是Integer.MAX_VALUE)。
<br />
[解读 Java 并发队列 BlockingQueue](https://javadoop.com/2017/08/22/java-concurrent-queue/?)

**在构建高可用的应用程序时，有界队列是一种强大的资源管理工具，它们能抑制并防止产生过多的工作项，使应用程序在负荷过载的情况下变得更加健壮。**


> java 6 新增两个容器类型 ： Deque (发音"deck") 和 BlockingDeque, 分别对Queue和BlockingQueue进行扩展。实现类包括 ArrayDeque 和 LinkedBlockingDeque。 Deque 是一个双端队列，实现了在队列头和队列尾高效插入和移除。<br /> 双端队列适用的模式是**工作密取(Work Stealing)**:在生产者-消费者模式中，所有消费者有一个共享的工作队列，在工作密取中，每个消费者都有各自的双端队列。如果一个消费者完成自己双端队列中的全部工作，那么它可以从其他消费者双端队列末尾秘密地获取工作。

------
线程状态转换：
![](https://github.com/CyC2018/CS-Notes/blob/master/pics/ace830df-9919-48ca-91b5-60b193f593d2.png)

> 阻塞方法和中断方法： 

线程阻塞(BLOCKED、WAITING、TIMED_WAITING)的一些原因： 
  - 等待I/O 操作结束
  - 等待获得锁
  - 等待从Thread.sleep方法中醒来
  - 等待另一个线程的计算结果

**阻塞操作与执行时间很长的普通操作的差别在于，被阻塞的线程必须等待某个不受它控制的事件发生后才能继续执行。当某个外部事件发生时，线程被置回RUNNABLE状态，并可以再次被调度执行。**

> 当某个方法抛出InterruptedException时，表示该方法是一个阻塞方法，如果这个方法被中断，那么它将努力提前结束阻塞状态。Thread提供interrupt方法，用于中断线程或者查询线程是否已经被中断。

> 中断是一种协作机制。一个线程不能强制其他线程停止正在执行的操作而去执行其他的操作。当线程A中断B时，A仅仅是要求B在执行到某个可以暂停的地方停止正在执行的操作，前提是线程B愿意停止下来。

> 同步工具类： 可以是任何一个对象，只要它根据自身的状态来协调线程的控制流。

- 闭锁：延迟线程的进度直到其到达终止状态，**到达结束状态后将不会再改变状态**。CountDownLatch：维护一个计数器(实际是AbstractQueuedSynchronizer的状态)，countDown()递减计数器，await()方法等待计数器达到0。

- FutureTask: 实现Future语义，表示一种抽象的可生产结果的计算。

Treiber stack : FutureTask中使用到了这种无锁并发栈,用来保存等待的线程，其实现方式是 CAS + 重试<br />
[FutureTask源码解读](http://www.cnblogs.com/micrari/p/7374513.html)

- Semaphore: 用来控制同时访问某个特定资源的操作数量，或同时执行某个指定操作的数量。

- 栅栏(Barrier): 阻塞一组线程直到某个事件发生。栅栏与闭锁的关键区别在于，所有线程必须到达了栅栏位置，才能继续执行。闭锁用于等待事件(事件完成，线程允许执行)，而栅栏用于等待其他线程(所有线程到达栅栏，允许继续执行后面的操作)。

 CyclicBarrier: 栅栏可以重置，多次使用。
 ```java
  public CyclicBarrier(int parties);
  public CyclicBarrier(int parties, Runnable barrierAction);
  
  /* Waits until all parties have invoked await on this barrier.*/
  public int await() throws InterruptedException, BrokenBarrierException；
 ```
<br />
Exchanger: 两方(Two-Party)栅栏

```java
//实现一个缓存器
public interface Computable<A, V> {
	V compute(A args) throws InterruptedException;
}

public class Memoizer<A,V> implements Computable<A,V>{
	private final ConcurrentHashMap<A,FutureTask<V>> cache = 
			new ConcurrentHashMap<>();
	
	private final Computable<A,V> comp;
	
	public Memoizer(Computable<A,V> comp) {
		this.comp = comp;
	}
	
	public V compute(A args) throws InterruptedException {
		
		while(true) {
			FutureTask<V> f = cache.get(args);
			
			if(f == null) {
				Callable<V> callable = new Callable<V>() {
					@Override
					public V call() throws InterruptedException {
						return comp.compute(args);
					}
				};
				
				FutureTask<V> ft = new FutureTask<>(callable);
				
				f = cache.putIfAbsent(args, ft);
				
				if(f == null) {
					f = ft;
					ft.run();
				}
			}
			
			try {
				return f.get();
			} catch(CancellationException e) {
				cache.remove(args, f);  // Cache Pollution, removed
			} catch (ExecutionException e) {
				e.printStackTrace();
			}
		}
	}
}
```

-------
> 无限制地创建线程的问题：
 - 线程生命周期的开销非常高；
 - 资源消耗；如果可运行的线程数量多于可用的处理器数量，那么有些线程将闲置。大量空闲的线程会占用许多内存，给垃圾回收器带来压力，而且大量线程在竞争CPU资源时还将产生其他性能开销。如果已经有足够多的线程使所有CPU保持忙碌状态，那么再创建更多线程反而会降低性能。
 - 稳定性；在可创建线程的数量上存在一个限制，如果破坏这些限制，可能会抛出OutOfMemoryError。

> Executor框架：任务是一组逻辑工作单元，而线程则是使任务异步执行的机制。在Java类库中，任务执行主要抽象不是Thread，而是Executor。**Executor基于生产者-消费者模式，提交任务的操作相当于生产者，执行任务的线程则相当于消费者。任务的提交和执行解耦。**
```java
public interface Executor {
    void execute(Runnable command);
}
```

> 线程池：通过调用Executors中的静态方法创建线程池

- newFixedThreadPool
- newCachedThreadPool
- newSingleThreadExecutor
- newScheduledThreadPool

> Executor生命周期： 
 
为了解决执行服务的生命周期问题，Executor扩展了ExecutorService接口,Executor生命周期有3中状态：运行、关闭、已终止。
```java
public interface ExecutorService extends Executor {
    void shutdown();
    List<Runnable> shutdownNow();
    boolean isShutdown();
    boolean isTerminated();
    Future<?> submit(Runnable task);
    <T> Future<T> submit(Runnable task, T result);
    <T> Future<T> submit(Callable<T> task);
    boolean awaitTermination(long timeout, TimeUnit unit)
        throws InterruptedException;
    <T> List<Future<T>> invokeAll(Collection<? extends Callable<T>> tasks)
        throws InterruptedException;
    <T> List<Future<T>> invokeAll(Collection<? extends Callable<T>> tasks,
                                  long timeout, TimeUnit unit)
        throws InterruptedException;
}
```

------
> Runnable 、 Callable
```java
public interface Runnable {
// 不能返回值，不能抛出异常
    public abstract void run();  
}

public interface Callable<V> {
    V call() throws Exception;
}

```


```java

public interface Future<V> {
	boolean cancel(boolean mayInterruptIfRunning);
	boolean isCancelled();
	boolean isDone();
	V get() throws InterruptedException, ExecutionException;
	V get(long timeout, TimeUnit unit)
       	 throws InterruptedException, ExecutionException, TimeoutException;
}

```

> CompletionService : 将 Executor 和 BlockingQueue 功能融合。ExecutorCompletionService 是其实现类。

------
> 任务取消：java中没有一种安全的抢占式方法来停止线程，因此也没有安全的抢占式方法来停止任务。只有一些协作式的机制，使请求取消的任务和代码都遵循一种协商好的协议。

**通常，中断是实现取消的最合理方式。**

> Thread中的中断方法：
 
```java
    public void interrupt(); // 中断目标线程
    public boolean isInterrupted(); // 返回目标线程的中断状态
    public static boolean interrupted(); // 清除当前线程的中断状态，并返回清除之前的值
    
```
中断操作并不会真正地中断一个正在运行的线程，而只是发出中断请求，然后由线程在下一个合适的时刻中断自己。

> JVM 关闭：JVM 既可以正常关闭，也可以强行关闭。

正常关闭的触发方式包括：
- 最后一个"正常(非守护)"线程结束
- 调用System.exit()
- 通过其他特定于平台的方法关闭(如发送SIGINT信号或键入 Ctrl-C)

强行关闭：调用 Runtime,halt 或者在操作系统中"kill" JVM 进程(如发送SIGKILL)。

> 关闭钩子: 

```java
Runtime.getRuntime().addShutdownHook(Thread hook);
```

> 守护线程(Daemon Thread)：线程分为两种：普通线程和守护线程。在 JVM 启动时创建的所有线程中，除了主线程以外，其他的线程都是守护线程(如垃圾回收器以及其他执行辅助工作的线程)。当创建一个新线程时，新线程将继承创建它的线程的守护状态，因此在默认情况下，主线程创建的所有线程都是普通线程。

普通线程和守护线程的差异仅在于当线程退出时发生的操作。当一个线程退出时，JVM会检查其他正在运行的线程，如果这些线程都是守护线程，那么JVM 会正常退出。当JVM 停止时，所有仍然存在的守护线程都将被抛弃(既不会执行finally代码块，也不会执行回卷栈，JVM只是直接退出)。

> finalize() ： **避免使用**

------

## 线程池： 
> 线程饥饿死锁(Thread Starvation Deadlock)：线程池中的任务需要无限期地等待一些必须由池中其他任务才能提供的资源或条件，除非线程池足够大，否则将发生线程饥饿死锁。

> 获取CPU数目：

```java
Runtime.getRuntime().availableProcessors();
```

> ThreadPoolExecutor:
 Executors中 newCachedThreadPool 和 newFixedThreadPool 返回的线程池都是 ThreadPoolExecutor 类型。
 
 **只有当任务相互独立时，为线程池或工作队列设置界限才是合理的。如果任务之间存在依赖性，那么有界的线程池或队列可能导致线程"饥饿"死锁问题。此时，应该使用无界的线程池，如 Executors.newCachedThreadPool()。**
 
> 饱和策略：当有界队列被填满后，饱和策略开始发挥作用(如果某个任务被提交到一个已被关闭的Executor,也会用到饱和策略)。

JDk提供的饱和策略(均实现了 RejectedExecutionHandler 接口)：
- AbortPolicy ： 默认策略，抛出 RejectedExecutionException
- CallerRunsPolicy ：Executes task in the caller's thread, unless the executor has been shut down, in which case the task is discarded.
- DiscardPolicy ：新提交的任务无法保存到队列中等待执行时，悄悄抛弃该任务，do nothing
- DiscardOldestPolicy ： 抛弃下一个将被执行的任务，然后尝试重新提交新任务

```java
//ThreadPoolExecutor通过调用该方法修改饱和策略
public void setRejectedExecutionHandler(RejectedExecutionHandler handler);

// RejectedExecutionHandler 接口定义
public interface RejectedExecutionHandler {
	void rejectedExecution(Runnable r, ThreadPoolExecutor executor);
}
```
