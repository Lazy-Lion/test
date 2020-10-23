

**linux 是多用户多任务的环境**

 ### centos 安装图形界面
   1. yum groupinstall "X Window System"
   2. yum groupinstall "GNOME Desktop"
   3. systemctl set-default graphical.target  设置默认启动图形界面
      systemctl set-default multi-user.target 设置默认启动命令行界面

 **linux文件路径使用 /**
 ### 指令集
 - 精简指令集 (Reduced Instruction Set Computer, RISC)
 - 复杂指令集 (Complex Instruction Set Computer, CISC) : intel公司最早的 8086，
 后来升级到32位，现在使用x86表示32位指令集，为了区分使用x86_64表示64位指令集

**各个组件和装置在Linux下都是一个文件**

 ### linux命令行格式 *command [-Option] parameter1 parameter2 ...*
  - *Option 当使用全称时使用 --, 如 **date --help** 命令*
  - *如果命令过长，可以使用\ + Enter，使指令连续到下一行*

### [root@localhost ~]# 
  - 登录到系统命名行界面后如上显示,其中~表示用户的家目录；如果是root用户表示的就是/root ( note: 根目录是 / )；如果是普通用户，如personal (自建的普通用户)，表示的就是/home/personal/；#是提示字符，root用户是#,普通用户是$;

**几乎所有的硬件设备文件都在/dev目录中**

### 几个简单指令
- su - : 切换至 root
- su - username : 切换至普通用户，用户名username
- echo : 显示
- mv : 文件移动
- date : 显示日期，
    *例 date +%Y/%m/%d : 以年/月/日 的形式显示日期，**可以看到某些特殊情况下，选项或参数前也会带 +***
- cal :  显示日历,
    *例 cal [month] [year] ：若没有参数，则显示当前月份的日历*
- cp : 复制命令
    *cp 来源文件 目的文件* 
- cd : 变更目录指令
- shutdown :关机指令，<br />
    *例 shutdown -h now **立刻关机***<br />
    *shutdown -h 20:25  **20:25关机***<br />
    *shutdown -h +10  **10分钟后关机***<br />
    *shutdown -h +10 "system will be shutdown" **10分钟后关机,并发出警告信息***
- poweroff : 关机指令
- reboot : 重启命令
- sync : 数据同步写入磁盘，一般情况下在使用shutdown指令时，系统默认会先执行sync，也可以手动执行
- uname -r : 查看核心版本
- uname -m : 查看操作系统位版本(64 or 32 位)

### 获取指令的帮助信息
 1. \-\-help
 2. man

 ```
  date  --help
  man date
 ```
 **使用man 得到的帮助信息中会显示有代号: 代号1 表示使用者在shell环境中可以使用的指令; 代号5表示配置文件格式；代号8表示系统管理员可用的管理指令**

 *说明文档的存放目录 ： /usr/share/doc*

### 几个快捷键
 - Tab : 命令补全，文件补全
 - Ctrl + c : 中断当前程序
 - Ctrl + d : 键盘输入结束，用来代替exit的输入
 - Shift + {[PageDown]|[PageUp]} : 命令行模式下的翻页

-----
### 权限管理（root基本上不受系统权限限制）
 - 拥有者
 - 群组
 - 其他人
 ```
   /*存放权限信息的文件*/
  /etc/passwd
  /etc/shadow
  /etc/group
 ```

 ##### 权限： rwx :分别表示 可读，可写，可执行
  - 显示权限信息的格式:
      *例 -rwxrwx---*
      第一个 - 表示档案类型：1. - 表示文件； 2. d 表示目录；3. l 表示链接文件；4. b 表示可供存储的周边设备； 5. c 表示序列埠设备，如鼠标、键盘;
    剩下的九个字符分三组，分别是拥有者权限，群组权限，其他人权限，rwx三种，如果有则用符号表示，否则使用 - 表示
 - 使用 ls -al 显示文档详细信息
    *例 -rw-r--r--. 1 root test 1864 May 4 18:01 initial-setup-ks.cfg*
    <br />
    -rw-r--r--： 权限信息<br />
    1 : 链接数<br />
    root : 拥有者<br />
    test : 所属群组<br />
    1864 : 档案容量<br />
    May 4 18:01 : 最后修改时间<br />
    initial-setup-ks.cfg : 文档名<br />

##### 权限相关命令
  - chgrp : 改变文件所属群组 
  - chown : 改变文件拥有者
  - chmod : 改变文件权限 ： 
    改变权限命令有多种使用方式，比较简单的是权值方式：r w x 分别使用 4 2 1 权值表示，如命令 chmod 664 .bashrc ，表示的即为 -rw-rw-r\-\-

##### 权限对于文件和目录的意义
> 文件：实际包含数据的地方，包括一般文本文件、数据库内容档、二进制可执行文件
><br />
>1.r (read): 可读取此文件的实际内容
><br />  
>2.w (write): 可以编辑、新增或修改文件的内容(**但不含删除该文件**)
><br />
>3.x (execute): 该文件具有可以被系统执行的权限。**在linux下，文件是否可以被执行，不是由文件的扩展名决定的，而是根据是否具有 x 权限决定的。(如windows的 .exe)**

>文件夹：记录文件名的清单<br />
> 1.r (read context in directory) : 可以查询该目录下的**文件名数据** <br />
> 2.w (modify context in directory) : 具有异动该目录结构清单的权限 => - 创建新的文件和目录， - 删除已经存在的文件和目录(不论该文件的权限为何)， - 将已存在的文件或目录改名， - 搬移该目录内的文件、目录位置<br />
>3.x (access directory) : 允许进入该目录作为工作目录  <br/>
-----
 ###### 关于目录和文件权限的举例
 <br />

  | 操作动作 | /dir1 | /dir1/file1 | /dir2 | info |
  | - | - | - | - | - |
  | 读取file1内容 | x | r | - | 先要进入dir1文件夹才能读取文件数据
  | 修改file1内容 | x | rw | - |
  | 执行file1内容 | x | rx | - |
  | 删除file1文件 | wx | - | - | 不需要对文件有权限
  | 将file1复制到/dir2 | x | r | wx | 


---
### 文件种类
 - 正规文件(regular file): ls -al 显示的属性第一个字符为 - ；可分为纯文本文件(ASCII)，二进制文件(Binary), 数据格式文件(data)
 - 目录(directory): ls -al 显示的属性第一个字符为 d
 - 链接文件(link): ls -al 显示的属性第一个字符为 l
 - 设备文件(device),与系统周边及存储等相关的文件，通常集中在/dev目录下，分为以下两种:区块(block)设备文件, 存储的设备，如/dev/sda，属性第一个字符 b ;字符(character)设备文件，如鼠标键盘，属性第一个字符 c
 - 数据接口文件(sockets),第一个属性为 s, 最常在/run 或 /tmp目录中看到这个文件类型
 - 数据输送档(FIFO，pipe),其主要目的在解决多个程序同时存取一个文件所导致的错误问题，第一个属性为 p;

### 文件扩展名
**linux文件名长度限制 255 Bytes**<br />
 linux 文件基本是没有扩展名的，一个linux文件能不能被执行，取决于权限，与文件名无关；linux可以通过扩展名表示文件的种类：
 - .sh : 脚本或批处理文件(scripts)
 -  Z, .tar, .tar.gz, .zip, *.tgz: 压缩文件
 - .html, .php : 网页相关文件

**文件名称的开头为小数点(.)时，代表这个文件是“隐藏文件”**

### linux 目录配置
**关于目录的详细，后续再补充**
  #### FHS(Filesystem Hierarchy Standard)标准：
   - / (根目录,root) : 与开机系统有关
   - /usr (unix software resource) : 与软件安装/执行有关
   - /var (variable) : 与系统运行过程有关

  #### 绝对路径和相对路径
- 绝对路径 : 由根目录(/)开始写起的文件名或目录名
- 相对路径 : 相对于目前工作路径的写法，两个特殊的符号：
    ```
        1. . ： 代表当前目录，也可以使用 ./ 来表示
        2. .. ：代表上一层目录，也可以使用 ../ 来表示
    ```

### 目录相关操作
<br />
*所有目录下都存在两个目录"."和"..",分别代表此层目录和上次目录；同样 / 根目录也存在这两个目录，这两个目录的属性和权限完全一致，表示根目录的上层目录和根目录自己是同一个目录*

##### 几个特殊的目录
```
 .  代表此层目录
 .. 代表上层目录
 -  代表前一个工作目录
 ~  代表目前使用者身份所在的主文件夹
 ~accout 代表accout这个使用者的主文件夹
```

##### 操作指令
- cd (change directory,变换目录)
- pwd (print working directory,显示当前目录): <br />
    [-P] :显示出确实的路径，而非显示链接路径
- mkdir (创建一个新的目录)：<br />
    [-m] :设置文件夹权限 <br />
    [-p] : 自动递归创建所需目录<br \>
  ```
   mkdir -m 744 -p test1/test2
    test1/test2 文件夹权限为 rwxr--r--
    test1 文件夹默认自动创建
  ```
- rmdir (删除**空**的目录): <br />
    [-p] :连同上层空的目录一起删除 <br />
    如果是非空目录 : rm -r 

##### 环境变量 PATH
```
    echo $PATH
```
----
### 文件与目录管理  
  *显示属性、拷贝、删除文件、移动文件或目录*
> ls : 文件与目录检视<br />

| Option | info |
| - | - |
| -a | 全部文件，连同隐藏文件(开头为 . 的文件)一起列出来 |
| -A | 全部文件，连同隐藏文件，但不包括 . 和 .. 这两个目录 |
| -d | 仅列出目录本身，而不是列出目录内的文件数据 |
| -f | 直接列出结果，而不进行排序(ls 默认会以文件名排序) |
| -F | 根据文件、目录等信息，给予附加数据结构,如： * 代表可执行文件； / 代表目录；= 代表socket文件; &#124; 代表FIFO文件； |
| -h | 将文件大小以较易读的方式列出来(如 GB，KB) |
| -i | 列出inode 号码(文件系统的组成，linux文件系统中介绍) |
| -l | 长数据串行出，包含文件的属性与权限等数据 |
| -n | 列出UID 与 GID， 而非使用者与群组名称 |
| -r | 将排序结果反向输出 |
| -R | 连同子目录内容一起列出来,等于该目录下的所有文件都会显示出来 |
| -S | 以文件大小排序,而不是以文件名排序 |
| -t | 依时间排序，而不是文件名 |
| \-\-color= never | 不要依据文件特性给予颜色显示 |
| \-\-color=always | 显示颜色 |
| \-\-color=auto | 让系统自行根据设置来判断是否给予颜色 |
| \-\-full-time | 以完整时间模式输出(包含年、月、日、时、分)
| \-\-time={atime,ctime} | 输出access 时间或改变权限属性时间(ctime)，而非内容变更时间(modification time) |

```
 ls -al ~
 ls -alF --color=never ~
```

> 复制、移动、删除(cp、 mv 、 rm)
 - cp (复制文件或目录) 

| Option | info |
| - | - |
| -a | 相当于 -dr \-\-preserve=all |
| -d | 若来源文件为链接文件的属性(link file)，则复制链接文件属性而非文件本身(*cp没有加上任何Option时，复制的是原始文件，而非链接文件的属性*) |
| -f | force，若目标文件已经存在且无法打开，则移除后再尝试一次 |
| -i | 若目标文件已经存在，在覆盖时会先询问动作的进行 |
| -l | 使用实体链接(hard link)的链接文件创建，而非复制文件本身 |
| -p | 连同文件的属性(权限、用户、时间)一起复制过去，而非使用默认属性 |
| -r | 递回持续复制，用于目录的复制行为 |
| -s | 复制成为符号链接文件(symbolic link)，亦即“捷径”文件 |
| -u | destination 比 source 旧才更新destination，或destination不存在时才复制 |
| \-\-preserve=all | 除了 -p 的权限相关参数外，还加入了SELinux的属性，links,xattr等也复制 |

 ```
    cp [Options] source1 source2 ... directory
    // 如果来源文件有两个及以上，最后一个目的文件一定要是目录
 ```
  **复制时需要特别注意目标文件或目录的权限**

 - rm (移除文件或目录)

| Option | Info |
| - | - |
| -f | force， 忽略不存在的文件，不会出现警告信息 |
| -i | 互动模式，在删除前会询问使用者是否动作 |
| -r | 递回删除，最常用在目录的删除 (**危险操作**) |

- mv (移动文件、目录，或更名)

| Option | Info |
| - | - |
| -f | force， 如果目标文件已经存在，不会询问而直接覆盖 |
| -i | 若目标文件已经存在，会询问是否覆盖 |
| -u | 若目标文件已经存在，且source比较新，才会更新(update) |

*mv 指令也可以有多个source,那么destination必须是目录*<br />
*linux下还有个更名指令 rename*

> basename 
> dirname

### 文件内容查阅

> cat (concatenate) : 由第一行开始显示文件内容

| Option | Info |
| - | - |
| -A | 相当于 -vET 的整合选项，可以列出一些特殊字符而不是空白而已 |
| -b | 列出行号, 仅针对非空白行做行号显示,空白行不标行号 |
| -E | 将结尾的断行字符 $ 显示出来 |
| -n | 打印出行号, 连同空白行也会有行号 |
| -T | 将[tab]按键以 ^I 显示出来 |
| -v | 列出一些看不出来的特殊字符 |

> tac ： 从最后一行开始显示,cat的倒着写

> nl ： 显示的时候，顺道输出行号

| Option | Info |
| - | - |
| -b | 指定行号指定的方式，有两种: <br /> -b a : 无论是否为空行，都列出行号;<br /> -b t : 如果是空行，不列出行号 |
| -n | 列出行号的表示方法，有三种：<br /> -n ln ：行号在屏幕最左方显示;<br /> -n rn ： 行号在自己字段的最右方显示，且不加0；<br /> -n rz : 行号在自己字段的最右方显示，且加0；
| -w | 行号字段的占用的字符数 |

```
 nl -b a -n rz -w 3 /etc/issue
```

> more ： 一页一页的显示文件内容

> less ：与more类似，但less可以往前翻页

> head ： 只看头几行

```
 head [-n number] filename
```

> tail ： 只看尾几行

| Option | Info |
| - | - |
| -n | 后面接数字，代表显示几行 |
| -f | 表示持续侦测文件，等到按下 ctrl + c 才会结束tail的侦测 (用于文件随时有数据写入，让该文件有数据写入时就显示在屏幕上) |

> od ： 以二进制的方式读取文件内容，不同于上面的命令，该命令可用于查阅非纯文本文件

```
 od [-t TYPE] file
```

| TYPE | Info |
| - | - |
| a | 利用默认的字符输出 |
| c | 利用ASCII 字符输出 |
| d[size] | 利用十进制(decimal)来输出数据，每个数据占用size Bytes |
| f[size] | 利用浮点数值(floating)来输出数据，每个数据占用size Bytes |
| o[size] | 利用八进制(octal)来输出数据，每个数据占用size Bytes |
| x[size] | 利用十六进制(hexadecimal)来输出数据，每个数据占用size Bytes |

> touch : 修改文件时间或创建新的空文件

 文件记录的三个主要的变动时间 ：
   1. modification time (mtime) : 当该文件的 "内容数据" 变更时，更新这个时间。内容数据指的是文件的内容，而不是文件的属性或权限；
   2. status time (ctime) : 当该文件的 "状态(status)" 改变时，更新这个时间，举例来说，像是权限和属性被更改了，都会更新这个时间；
   3. access time (atime) : 当 "该文件的内容被取用" 时，更新这个时间。如使用cat读取时；

```
 touch [Option] file
```
| Option | Info |
| - | - |
| -a | 仅修订access time |
| -c | 仅修改文件的时间，若该文件不存在，不创建新文件 |
| -d | 后面可接欲修订的日期而不用目前的日期，也可使用 --date="日期或时间" |
| -m | 仅修改 mtime |
| -t | 后面可接欲修订的时间而不用目前的时间,格式为 [YYYYMMDDhhmm]

*ctime 记录的是文件最近的状态被改变的时间， -d -t 设置的时间都不会改动到ctime,ctime会自动更新*

## 文件与目录的默认权限和隐藏权限
> 文件默认权限 ： -rw-rw-rw-  => 666
> 目录默认权限 ： drwxrwxrwx  => 777

```
  umask :  显示的是默认权限值需要减掉的值, 如022 则创建目录时权限为u=rwx,g=r-x,o=r-x
  umask  也可以自行设置，如 umask 002
  umask -S : 以符号方式显示
```

> 隐藏权限
 - chattr ：设置文件隐藏属性
 - lsattr ：显示文件隐藏属性

> 文件特殊权限
 - SUID
 - SGID
 - SBIT

> file 指令：观察文件类型,用来简单判断文件格式

```
 file /etc/issue
```

### 文件搜索
> which : 寻找可执行文件

```
    which [-a] command :
      -a : 将所有由 PATH 目录中找到的指令均列出，而不止第一个被找到的指令名称
```

> whereis : 由一些特定的目录中寻找文件

 ```
    whereis [Option] filename or dirname
 ```

| Option | Info |
| - | - |
| -l | 列出whereis 会去查询的几个主要目录 |
| -b | 只找 binary 格式的文件 |
| -m | 只找在说明文档 manual 路径下的文件 |
| -s | 只找 source 来源文件 |
| -u | 搜索不在上述三个项目中的其他特殊文件 |

> locate/updatedb

```
 locate [Option] keyword
```

| Option | Info |
| - | - |
| -i | 忽略大小写的差异 |
| -c | 不输出文件名，仅计算找到的文件数量 |
| -l | 仅输出几行,如 -l 5 即仅输出5行
| -S | 输出 locate 所使用的数据库文件的相关信息，包括该数据库记录的文件/目录数量等 |
| -r | 后面可接正则表达式的显示方式 |

**updatedb指令 手动更新locate命令搜索时使用的数据库，更新依据/etc/updatedb.conf的设置**

> find :

```
 find [PATH] [Option] [action]
```

| | Option | Info |
| - | - | - |
| 与时间有关的选项(-atime,-ctime,-mtime)| -mtime n | n -> n + 1 天被改动的文件 |
| | -mtime +n | 大于等于 n + 1 天前被改动的文件|
| | -mtime -n | 小于等于 n 天被改动的文件 |
| | -newer file | file为一个存在文件，列出比file 还要新的文件文件名 |
| 与使用者或群组名称相关 | -uid n | n为数字，是使用者账号 ID |
| | -gid n | n为数字，是群组名称 ID |
| | -user name | name 为使用者账号名称 |
| | -group name | name为群组名称 |
| | -nouser | 寻找文件的拥有者不存在 /etc/passwd |
| | -nogroup | 寻找文件的拥有群组不存在与 /etc/group  |
| 与文件权限及名称相关 | -name filename | 搜索文件名称为filename的文件 |
| | -size [+\-]SIZE | 搜索比SIZE大(+)或小(-)的文件, 规格： c => Byte ,k => 1024Bytes ,如 -size +50k |
| | -type TYPE | 搜索文件类型为TYPE (f,b,c,d,l,s,p)|
| | -perm mode | 搜索文件权限是mode的文件 |
| | -perm -mode | 搜索文件权限包括mode的文件 |
| | -perm /mode | 搜索文件权限"包含任一 mode 的权限"的文件 |


### 文件系统的简单操作
> df ：列出文件系统的整体磁盘使用量

```
 df [Option] [filename or dirname]
```
| Option | Info |
| - | - |
| -a | 列出所有的文件系统，包括系统特有的 /proc 等文件系统 |
| -k | 以 KBytes 的容量显示各文件系统 |
| -m | 以 MBytes 的容量显示各文件系统 |
| -h | 以人们较易阅读的 GBytes, MBytes, KBytes 等格式自行显示 |
| -H | 以M=1000K 取代 M=1024的进位方式 |
| -T | 连同 partition 的 filesystem 名称 (如 xfs) 也列出 |
| -i | 不用磁盘容量，而以 inode 的数量来显示 |

> du 

```
 du [Option] [filename or dirname]
```

| Option | Info |
| - | - |
| -a | 列出所有的文件与目录容量，因为默认仅统计目录下面的文件量而已 |
| -h | 以人们较易读的容量格式 (G/M) 显示 |
| -s | 列出总量，而不列出每个个别的目录占用容量 |
| -S | 不包括子目录下的总计 |
| -k | 以 KBytes 列出容量显示 |
| -m | 以 MBytes 列出容量显示 |

### 链接文件
> Hard Link (实体链接，硬式链接或实际链接)
 - 每个文件都会占用一个inode，文件内容有inode的记录来指向
 - 想要读取该文件，必须要经过目录记录的文件名来指向到正确的inode号码才能读取
 *文件名只与目录有关，文件内容与inode有关*<br />
 hard link 是某个目录下新增一笔文件名链接到某个inode号码的关联记录。即多个文件名指向同一个inode，除了文件名以外，其他相关信息都一样。
 <br />

 ###### hard link的限制：
  - 不能跨Filesystem
  - 不能link目录

> Symbolic Link (符号链接, 亦即是捷径)：
   Symbolic link 就是在创建一个**独立的文件**，而这个文件会让数据的读取指向它link的那个文件的文件名
> ln 

```
 ln [Option] 来源文件 目标文件
 ln /tmp/passwd /tmp/passwd_hdlink
```
| Option | Info |
| - | - |
| -s | 如果不加任何参数就进行链接，就是hard link, -s 就是symbolic link |
| -f | 如果目标文件存在，就主动将目标文件直接移除后再创建 |

### Ext2文件系统
 数据存取为索引式文件系统 (日志式文件系统会多出一块记录区，随时记录文件系统的主要活动，可加快系统复原时间)

 - superblock : 记录此filesystem的整体信息, 包括inode/block的总量、使用量、剩余量，以及文件系统的格式与相关信息等； 
 - inode : 记录文件的属性，一个文件占用一个inode，同时记录此文件的数据所在的block号码；
 - block : 实际记录文件的内容，若文件太大时，会占用多个block

### swap ： 内存交换空间
   暂时将内存的程序拿到硬盘中存放

### 文件压缩

| 扩展名 | 说明 |
| - | - |
| *.Z | compresss 程序压缩的文件 |
| *.zip | zip 程序压缩的文件 |
|*.gz | gzip 程序压缩的文件 |
| *.bz2 | bzip2 程序压缩的文件 |
| *.xz | xz程序压缩的文件 |
| *.tar | tar 程序打包的数据，并没有压缩过 |
| *.tar.gz | tar 程序打包的文件，并且经过 gzip 的压缩 |
| *.tar.bz2 | tar 程序打包的文件，并且经过 bzip2 的压缩 |
| *.tar.xz | tar 程序打包的文件，并经过 xz 的压缩 |

 > gzip [-cdtv#] 文件名

  **当使用gzip进行压缩时，在默认的状态下原本的文件会被压缩成.gz的文件名，原始文件就不存在了。**

| Option | Info |
| - | - |
| -c | 将压缩的数据输出到屏幕上，可通过数据流重导向来处理 |
| -d | 解压缩的参数 |
| -t | 可以用来检验一个压缩文件的一致性，看文件有无错误 |
| -v | 可以显示出原文件/压缩文件的压缩比信息 |
| -# | # 为数字的意思，代表压缩等级，-1最快，但压缩比最差；-9 最慢，但压缩比最好；默认是-6 |

 zcat/zmore/zless 可以读取gzip压缩的文本文件的原始文件内容
 zgrep 查找gzip的原始文件中的数据

 > bzip2 [-cdkzv#] 文件名

| Option | Info |
| - | - |
| -c | 将压缩的过程产生的数据输出到屏幕上 |
| -d | 解压缩的参数 |
| -k | 保留原始文件 |
| -z | 压缩的参数(默认值，可以不加) |
| -v | 可以显示出原文件/压缩文件的压缩比等信息 |
| -# | 与 gzip 一致 |

 bzcat/bzmore/bzless/bzgrep

 > xz [-dtlkc#] 文件名

 压缩效果好，但相当耗时。

| Option | Info |
| - | - |
| -d | 解压缩的参数 |
| -t | 册数压缩文件的完整性，看有没有错误 |
| -l | 列出压缩文件的相关信息 |
| -k | 保留原始文件 |
| -c | 将压缩的过程产生的数据输出到屏幕上 |
| -# | 与 gzip 一致 |

 xzcat/xzmore/xzless/xzgrep

 ### 文件打包

 将多个目录或文件打包成一个大文件

 ```
  tar [-z|-j|-J] [cv] [-f 待创建的新文件名] filename ： 打包
  tar [-z|-j|-J] [tv] [-f 既有的 tar 文件名] : 查看
  tar [-z|-j|-J] [xv] [-f 既有的 tar 文件名] [-C 目录] ： 解压
 ```
| Option | Info |
| - | - |
| -c | 创建打包文件,可搭配 -v 来查看过程中被打包的文件名(filename) |
| -t | 查看打包文件的内容含有那些文件名 |
| -x | 解打包或解压缩，可以搭配 -C 在特定目录解开 |
| -z | 通过 gzip 的支持进行压缩/解压缩 |
| -j | 通过 bzip2 的支持进行压缩/解压缩 |
| -J | 通过 xz 的支持进行压缩/解压缩 |
| -v | 在压缩/解压缩的过程中，将正在处理的文件名显示 |
| -f filename| -f 后要立刻接要被处理的文件名， 建议 -f 单独写一个选项 |
| -C 目录 | 这个选项用在解压缩，若要在特定目录解压缩，可以使用这个选项 |
| -p | 保留备份数据的原本权限与属性，常用于备份(-c)重要的配置文件 |
| -P | 保留绝对路径，亦即允许备份数据中含有根目录存在,**最好不要使用** |
| \-\-exclude=PATTERN <br />| 在压缩过程中，去除指定模式的文件 |
| \-\-newer | |
| \-\-newer-mtime | |

 解压时指定文件名，可以只解压一个文件。

### Vim 
- 一般指令模式(commadn mode) :
 以vi打开一个文件直接进入，可以使用 “上下左右”按键来移动光标，可以使用 “删除字符”或“删除整列”来处理文件内容，也可以进行“复制”、“粘贴”处理。
- 编辑模式 (insert mode) :
 一般指令模式无法编辑文件内容，按下 "i" 后进入编辑模式，如果要回到一般指令模式，按 "Esc".
- 命令行模式(command-line mode) :
 一般模式中输入 shift + ; , 按 "Esc" 退回到一般模式。

| 命令行模式指令 | 说明 |
| - | - |
| :w | 将编辑的数据写入磁盘文件 |
| :w! | 若文件属性为 "只读"，强制写入该文件，不过到底能不能写入，还是跟你对该文件的文件权限有关 |
| :q | 离开 vi |
| :q! | 若修改过文件，又不想储存，使用 ! 强制离开，不存储 ； ! 在 vi 中常有 “强制” 的意思 |
| :wq | 储存后离开，:wq! 为强制储存后离开 |

 

 # Reference 

[鸟哥linux私房菜 基础篇 第四版](http://oqo3t056d.bkt.clouddn.com/vbird-linux-basic-4e.pdf)

