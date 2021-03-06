### Java Object 类的方法

```java
public final native Class<?> getClass()//native方法，用于返回当前运行时对象的Class对象，使用了final关键字修饰，故不允许子类重写。

public native int hashCode() //native方法，用于返回对象的哈希码，主要使用在哈希表中，比如JDK中的HashMap。
public boolean equals(Object obj)//用于比较2个对象的内存地址是否相等，String类对该方法进行了重写用户比较字符串的值是否相等。

protected native Object clone() throws CloneNotSupportedException//naitive方法，用于创建并返回当前对象的一份拷贝。一般情况下，对于任何对象 x，表达式 x.clone() != x 为true，x.clone().getClass() == x.getClass() 为true。Object本身没有实现Cloneable接口，所以不重写clone方法并且进行调用的话会发生CloneNotSupportedException异常。

public String toString()//返回类的名字@实例的哈希码的16进制的字符串。建议Object所有的子类都重写这个方法。

public final native void notify()//native方法，并且不能重写。唤醒一个在此对象监视器上等待的线程(监视器相当于就是锁的概念)。如果有多个线程在等待只会任意唤醒一个。

public final native void notifyAll()//native方法，并且不能重写。跟notify一样，唯一的区别就是会唤醒在此对象监视器上等待的所有线程，而不是一个线程。

public final native void wait(long timeout) throws InterruptedException//native方法，并且不能重写。暂停线程的执行。注意：sleep方法没有释放锁，而wait方法释放了锁 。timeout是等待时间。

public final void wait(long timeout, int nanos) throws InterruptedException//多了nanos参数，这个参数表示额外时间（以毫微秒为单位，范围是 0-999999）。 所以超时的时间还需要加上nanos毫秒。

public final void wait() throws InterruptedException//跟之前的2个wait方法一样，只不过该方法一直等待，没有超时时间这个概念

protected void finalize() throws Throwable { }//实例被垃圾回收器回收的时候触发的操作
```

### 基本类型运算

```java
        int a = 2;
        double b = 2.0;
        System.out.print(a == b);
```

基本类型的二元操作，存在类型自动提升。上述代码的核心字节码如下：

```java
         9: iload_1
        10: i2d
        11: dload_2
        12: dcmpl
        13: ifne          20
        16: iconst_1
        17: goto          21
        20: iconst_0
```

提升规则：
　　如果两个操作数其中有一个是double类型，另一个操作就会转换为double类型。
　　否则，如果其中一个操作数是float类型，另一个将会转换为float类型。
　　否则，如果其中一个操作数是long类型，另一个会转换为long类型。
　　否则，两个操作数都转换为int类型。

``` java
        byte a = 1;
        // byte b = a + a; // Incompatible types. Required: int; Found: int
        a += 1;
```

```java
         0: iconst_1
         1: istore_1
         2: iload_1
         3: iconst_1
         4: iadd
         5: i2b    // a += 1 在操作结束后会做一次类型转换，转成byte
         6: istore_1

```

### 泛型

协变、逆变

Maven使用JDK 1.8

```xml
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-compiler-plugin</artifactId>
                <version>3.5.1</version>
                <configuration>
                    <source>1.8</source>
                    <target>1.8</target>
                </configuration>
            </plugin>
```

