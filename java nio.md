# Java NIO

| IO              | NIO             |
| --------------- | --------------- |
| Stream-oriented | Block-oriented |
| Blocking IO | Selectors (Non-blocking IO) |

# Stream-oriented vs. Block-oriented
A *stream-oriented* I/O system deals with data one byte at a time. An input stream produces one byte of data, and an output stream consumes one byte of data. It is very easy to create filters for streamed data. It is also relatively simply to chain several filters together so that each one does its part in what amounts to a single, sophisticated processing mechanism. On the flip side, stream-oriented I/O is often rather slow.

A *block-oriented* I/O system deals with data in blocks. Each operation produces or consumes a block of data in one step. Processing data by the block can be much faster than processing it by the (streamed) byte. But block-oriented I/O lacks some of the elegance and simplicity of stream-oriented I/O.

# Channel and Buffer

`Channel` and `Buffer` are the central objects in NIO, and are used for just about every I/O operation. 

**Channels are analogous to streams in the original I/O package.** All data that goes anywhere (or comes from anywhere) must pass through a `Channel` object. **A `Buffer` is essentially a container object.** All data that is sent to a channel must first be placed in a buffer; likewise, any data that is read from a channel is read into a buffer.

### Kinds of buffers

- `ByteBuffer`
- `CharBuffer`
- `ShortBuffer`
- `IntBuffer`
- `LongBuffer`
- `FloatBuffer`
- `DoubleBuffer`

### Kinds of channels

Channels differ from streams in that they are bi-directional. Whereas streams only go in one direction (a stream must be a subclass of either `InputStream` or `OutputStream` ), a `Channel` can be opened for reading, for writing, or for both.

```java
import java.io.*;
import java.nio.*;
import java.nio.channels.*;

public class CopyFile
{
  public static void main( String args[] ) throws Exception {
    if (args.length<2) {
      System.err.println( "Usage: java CopyFile infile outfile" );
      System.exit( 1 );
    }

    String infile = args[0];
    String outfile = args[1];

    FileInputStream fin = new FileInputStream( infile );
    FileOutputStream fout = new FileOutputStream( outfile );

    FileChannel fcin = fin.getChannel();
    FileChannel fcout = fout.getChannel();

    ByteBuffer buffer = ByteBuffer.allocate( 1024 );
    /**
    * ByteBuffer buffer = ByteBuffer.allocate( 1024 );
    *
    * ByteBuffer buffer = ByteBuffer.wrap( new byte[1024] );
    */

    while (true) {
      buffer.clear();

      int r = fcin.read( buffer );

      if (r==-1) {
        break;
      }

      buffer.flip();

      fcout.write( buffer );
    }
  }
}
```

### Buffer internals

1. We’ll start with a newly created buffer, which has a total `capacity` of eight bytes.  Because the `capacity` is not going to change, we can omit it from the discussion that follows.

![Position setting](https://developer.ibm.com/developer/default/tutorials/j-nio/images/figure3.gif)

2. The first read gets three bytes.

![Position increased to 3](https://developer.ibm.com/developer/default/tutorials/j-nio/images/figure4.gif)

3. For our second read, we read two more bytes from the input channel into our buffer.

![Position increased by 2](https://developer.ibm.com/developer/default/tutorials/j-nio/images/figure5.gif)

4. Now we are ready to write our data to an output channel. Before we can do this, we must call the `flip()` method. This method does two crucial things:

   - It sets the `limit` to the current `position`.

   - It sets the `position` to 0.

   

   ![Buffer after the flip](https://developer.ibm.com/developer/default/tutorials/j-nio/images/figure6.gif)

5. In our first write, we take four bytes from the buffer and write them to our output channel.

![Code limit unchanged](https://developer.ibm.com/developer/default/tutorials/j-nio/images/figure7.gif)

6. We only have one byte left to write.

![Code limit unchanged](https://developer.ibm.com/developer/default/tutorials/j-nio/images/figure8.gif)

7. Our final step is to call the buffer’s `clear()` method. This method resets the buffer in preparation for receiving more bytes. `Clear` does two crucial things:

   - It sets the `limit` to match the `capacity`.

   - It sets the `position` to 0.

   ![Buffer after clear has been called](https://developer.ibm.com/developer/default/tutorials/j-nio/images/figure9.gif)

### Buffer slicing and data sharing

```java
ByteBuffer buffer = ByteBuffer.allocate( 10 );

for (int i=0; i<buffer.capacity(); ++i) {
     buffer.put( (byte)i );
}

buffer.position( 3 );
buffer.limit( 7 );
ByteBuffer slice = buffer.slice();
```

`slice` is a sub-buffer of `buffer`. However, `slice` and `buffer` share the same underlying data array.

### Read-only buffers

 You can turn any regular buffer into a read-only buffer by calling its `asReadOnlyBuffer()` method, which returns a new buffer that is identical to the first (and shares data with it), but is read-only.

You cannot convert a read-only buffer to a writable buffer.

### Direct and indirect buffers

*Given a direct byte buffer, the Java virtual machine will make a best effort to perform native I/O operations directly upon it. That is, it will attempt to avoid copying the buffer’s content to (or from) an intermediate buffer before (or after) each invocation of one of the underlying operating system’s native I/O operations.*

```java
    ByteBuffer buffer = ByteBuffer.allocateDirect( 1024 );
```

You can also create a direct buffer using memory-mapped files.

Memory-mapped file I/O is a method for reading and writing file data that can be a great deal faster than regular stream- or channel-based I/O.

```java
MappedByteBuffer mbb = fc.map( FileChannel.MapMode.READ_WRITE, 0, 1024 ); // map a FileChannel (all or a portion of it) into memory.
```

# Scattering and gathering

Scatter/gather I/O is a method of reading and writing that uses multiple buffers, rather than a single buffer, to hold data.

A scattering read is like a regular channel read, except that it reads data into an array of buffers rather than a single buffer. Likewise, a gathering write writes data from an array of buffers rather than a single buffer.

Scatter/gather I/O is useful for dividing a data stream into separate sections, which can help implement complicated data formats.

```java
import java.io.*;
import java.net.*;
import java.nio.*;
import java.nio.channels.*;

public class UseScatterGather {
    static private final int firstHeaderLength = 2;
    static private final int secondHeaderLength = 4;
    static private final int bodyLength = 6;

    static public void main(String args[]) throws Exception {
        if (args.length != 1) {
            System.err.println("Usage: java UseScatterGather port");
            System.exit(1);
        }

        int port = Integer.parseInt(args[0]);

        ServerSocketChannel ssc = ServerSocketChannel.open();
        InetSocketAddress address = new InetSocketAddress(port);
        ssc.socket().bind(address);

        int messageLength =
                firstHeaderLength + secondHeaderLength + bodyLength;

        ByteBuffer buffers[] = new ByteBuffer[3];
        buffers[0] = ByteBuffer.allocate(firstHeaderLength);
        buffers[1] = ByteBuffer.allocate(secondHeaderLength);
        buffers[2] = ByteBuffer.allocate(bodyLength);

        SocketChannel sc = ssc.accept();

        while (true) {

            // Scatter-read into buffers
            int bytesRead = 0;
            while (bytesRead < messageLength) {
                long r = sc.read(buffers);
                bytesRead += r;

                System.out.println("r " + r);
                for (int i = 0; i < buffers.length; ++i) {
                    ByteBuffer bb = buffers[i];
                    System.out.println("b " + i + " " + bb.position() + " " + bb.limit());
                }
            }

            // Process message here

            // Flip buffers
            for (int i = 0; i < buffers.length; ++i) {
                ByteBuffer bb = buffers[i];
                bb.flip();
            }

            // Scatter-write back out
            long bytesWritten = 0;
            while (bytesWritten < messageLength) {
                long r = sc.write(buffers);
                bytesWritten += r;
            }

            // Clear buffers
            for (int i = 0; i < buffers.length; ++i) {
                ByteBuffer bb = buffers[i];
                bb.clear();
            }

            System.out.println(bytesRead + " " + bytesWritten + " " + messageLength);
        }
    }
}
```

# File locking

 File locks are just like regular Java object locks — they are *advisory* locks. They don’t prevent any kind of data access; instead, they allow different parts of a system to coordinate through the sharing and acquisition of locks.

```java
import java.io.*;
import java.nio.*;
import java.nio.channels.*;

public class UseFileLocks {
    static private final int start = 10;
    static private final int end = 20;

    static public void main(String args[]) throws Exception {
        // Get file channel
        RandomAccessFile raf = new RandomAccessFile("usefilelocks.txt", "rw");
        FileChannel fc = raf.getChannel();

        // Get lock
        System.out.println("trying to get lock");
        FileLock lock = fc.lock(start, end, false);
        System.out.println("got lock!");

        // Pause
        System.out.println("pausing");
        try {
            Thread.sleep(3000);
        } catch (InterruptedException ie) {
        }

        // Release lock
        System.out.println("going to release lock");
        lock.release();
        System.out.println("released lock");

        raf.close();
    }
}
```

File locking can be tricky business, especially given the fact that different operating systems implement locks differently. The following guidelines will help you keep your code as portable as possible:

- Only use exclusive locks.
- Treat all locks as advisory.

# Networking IO

### Selectors

Java NIO's selectors allow a single thread to monitor multiple channels of input. You can register multiple channels with a selector, then use a single thread to "select" the channels that have input available for processing, or select the channels that are ready for writing. **This selector mechanism makes it easy for a single thread to manage multiple channels.**

### Blocking vs. Non-blocking (Java Selector提供一种非阻塞的IO模式)

Java IO's various streams are blocking. That means, that when a thread invokes a `read()` or `write()`, that thread is blocked until there is some data to read, or the data is fully written. The thread can do nothing else in the meantime.

Java NIO's non-blocking mode enables a thread to request reading data from a channel, and only get what is currently available, or nothing at all, if no data is currently available. Rather than remain blocked until data becomes available for reading, the thread can go on with something else.

The same is true for non-blocking writing. 

```java
import java.io.*;
import java.net.*;
import java.nio.*;
import java.nio.channels.*;
import java.util.*;

public class MultiPortEcho {
    private int ports[];
    private ByteBuffer echoBuffer = ByteBuffer.allocate(1024);

    public MultiPortEcho(int ports[]) throws IOException {
        this.ports = ports;

        go();
    }

    private void go() throws IOException {
        // Create a new selector
        Selector selector = Selector.open();

        // Open a listener on each port, and register each one
        // with the selector
        for (int i = 0; i < ports.length; ++i) {
            ServerSocketChannel ssc = ServerSocketChannel.open();
            ssc.configureBlocking(false);
            ServerSocket ss = ssc.socket();
            InetSocketAddress address = new InetSocketAddress(ports[i]);
            ss.bind(address);

            SelectionKey key = ssc.register(selector, SelectionKey.OP_ACCEPT);

            System.out.println("Going to listen on " + ports[i]);
        }

        while (true) {
            int num = selector.select();

            Set selectedKeys = selector.selectedKeys();
            Iterator it = selectedKeys.iterator();

            while (it.hasNext()) {
                SelectionKey key = (SelectionKey) it.next();

                if ((key.readyOps() & SelectionKey.OP_ACCEPT)
                        == SelectionKey.OP_ACCEPT) {
                    // Accept the new connection
                    ServerSocketChannel ssc = (ServerSocketChannel) key.channel();
                    SocketChannel sc = ssc.accept();
                    sc.configureBlocking(false);

                    // Add the new connection to the selector
                    SelectionKey newKey = sc.register(selector, SelectionKey.OP_READ);
                    it.remove();

                    System.out.println("Got connection from " + sc);
                } else if ((key.readyOps() & SelectionKey.OP_READ)
                        == SelectionKey.OP_READ) {
                    // Read the data
                    SocketChannel sc = (SocketChannel) key.channel();

                    // Echo data
                    int bytesEchoed = 0;
                    while (true) {
                        echoBuffer.clear();

                        int r = sc.read(echoBuffer);

                        if (r <= 0) {
                            break;
                        }

                        echoBuffer.flip();

                        sc.write(echoBuffer);
                        bytesEchoed += r;
                    }

                    System.out.println("Echoed " + bytesEchoed + " from " + sc);

                    it.remove();
                }

            }

//System.out.println( "going to clear" );
//      selectedKeys.clear();
//System.out.println( "cleared" );
        }
    }

    static public void main(String args[]) throws Exception {
        if (args.length <= 0) {
            System.err.println("Usage: java MultiPortEcho port [port port ...]");
            System.exit(1);
        }

        int ports[] = new int[args.length];

        for (int i = 0; i < args.length; ++i) {
            ports[i] = Integer.parseInt(args[i]);
        }

        new MultiPortEcho(ports);
    }
}

```

# Charset

```java
import java.io.*;
import java.nio.*;
import java.nio.channels.*;
import java.nio.charset.*;

public class UseCharsets {
    static public void main(String args[]) throws Exception {
        String inputFile = "samplein.txt";
        String outputFile = "sampleout.txt";

        RandomAccessFile inf = new RandomAccessFile(inputFile, "r");
        RandomAccessFile outf = new RandomAccessFile(outputFile, "rw");
        long inputLength = new File(inputFile).length();

        FileChannel inc = inf.getChannel();
        FileChannel outc = outf.getChannel();

        MappedByteBuffer inputData =
                inc.map(FileChannel.MapMode.READ_ONLY, 0, inputLength);

        Charset latin1 = Charset.forName("ISO-8859-1");
        CharsetDecoder decoder = latin1.newDecoder();
        CharsetEncoder encoder = latin1.newEncoder();

        CharBuffer cb = decoder.decode(inputData);

        // Process char data here

        ByteBuffer outputData = encoder.encode(cb);

        outc.write(outputData);

        inf.close();
        outf.close();
    }
}
```

# Reference

[Java NIO vs IO](http://tutorials.jenkov.com/java-nio/nio-vs-io.html#main-differences-between-java-nio-and-io)
[Getting started with new I/O (NIO)](https://developer.ibm.com/languages/java/tutorials/j-nio/?mhsrc=ibmsearch_a&mhq=java%20nio&_ga=2.262063882.682083932.1603089350-864276855.1603089350)
[文件锁](https://zhuanlan.zhihu.com/p/25134841)