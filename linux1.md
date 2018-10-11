# 图侦平台
# 海燕系统
# 视频质量轮巡考核系统

[VMWare Download](http://www.zdfans.com/html/5928.html)

[鸟哥linux私房菜 基础篇 第四版](http://oqo3t056d.bkt.clouddn.com/vbird-linux-basic-4e.pdf)

# VMware 2018 v14.x 永久许可证激活密钥
 - FF31K-AHZD1-H8ETZ-8WWEZ-WUUVA
 - CV7T2-6WY5Q-48EWP-ZXY7X-QGUWD

# linux 
 ## centos 安装图形界面
   1. yum groupinstall "X Window System"
   2. yum groupinstall "GNOME Desktop"
   3. systemctl set-default graphical.target  设置默认启动图形界面
      systemctl set-default multi-user.target 设置默认启动命令行界面

 *linux文件路径使用 /*
 ## 指令集
 - 精简指令集 (Reduced Instruction Set Computer, RISC)
 - 复杂指令集 (Complex Instruction Set Computer, CISC) : intel公司最早的 8086，
 后来升级到32位，现在使用x86表示32位指令集，为了区分使用x86_64表示64位指令集
 
<br />

**各个组件和装置在Linux下都是一个文件**

 ## linux命令行格式 *command [-Option] parameter1 parameter2 ...*
  - *Option 当使用全称时使用 --, 如 **date --help** 命令*
  - *如果命令过长，可以使用\ + Enter，使指令连续到下一行*
  
## [root@localhost ~]# 
  - 登录到系统命名行界面后如上显示,其中~表示用户的家目录；如果是root用户表示的就是/root ( note: 根目录是 / )；如果是普通用户，如personal (自建的普通用户)，表示的就是/home/personal/；#是提示字符，root用户是#,普通用户是$;

**几乎所有的硬件设备文件都在/dev目录中**

## 几个简单指令
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

## 获取指令的帮助信息
 1. \-\-help
 2. man
 
例
 ```
  date  --help
  man date
 ```
 **使用man 得到的帮助信息中会显示有代号: 代号1 表示使用者在shell环境中可以使用的指令; 代号5表示配置文件格式；代号8表示系统管理员可用的管理指令**
 
 *说明文档的存放目录 ： /usr/share/doc*

## 几个快捷键
 - Tab : 命令补全，文件补全
 - Ctrl + c : 中断当前程序
 - Ctrl + d : 键盘输入结束，用来代替exit的输入
 - Shift + {[PageDown]|[PageUp]} : 命令行模式下的翻页

-----
## 权限管理（root基本上不受系统权限限制）
 - 拥有者
 - 群组
 - 其他人
 ```
   /*存放权限信息的文件*/
  /etc/passwd
  /etc/shadow
  /etc/group
 ```
 
 #### 权限： rwx :分别表示 可读，可写，可执行
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

#### 权限相关命令
  - chgrp : 改变文件所属群组 
  - chown : 改变文件拥有者
  - chmod : 改变文件权限 ： 
    改变权限命令有多种使用方式，比较简单的是权值方式：r w x 分别使用 4 2 1 权值表示，如命令 chmod 664 .bashrc ，表示的即为 -rw-rw-r\-\-
   
#### 权限对于文件和目录的意义
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
## 文件种类
 - 正规文件(regular file): ls -al 显示的属性第一个字符为 - ；可分为纯文本文件(ASCII)，二进制文件(Binary), 数据格式文件(data)
 - 目录(directory): ls -al 显示的属性第一个字符为 d
 - 链接文件(link): ls -al 显示的属性第一个字符为 l
 - 设备文件(device),与系统周边及存储等相关的文件，通常集中在/dev目录下，分为以下两种:区块(block)设备文件, 存储的设备，如/dev/sda，属性第一个字符 b ;字符(character)设备文件，如鼠标键盘，属性第一个字符 c
 - 数据接口文件(sockets),第一个属性为 s, 最常在/run 或 /tmp目录中看到这个文件类型
 - 数据输送档(FIFO，pipe),其主要目的在解决多个程序同时存取一个文件所导致的错误问题，第一个属性为 p;

## 文件扩展名
**linux文件名长度限制 255 Bytes**<br />
 linux 文件基本是没有扩展名的，一个linux文件能不能被执行，取决于权限，与文件名无关；linux可以通过扩展名表示文件的种类：
 - .sh : 脚本或批处理文件(scripts)
 -  Z, .tar, .tar.gz, .zip, *.tgz: 压缩文件
 - .html, .php : 网页相关文件

**文件名称的开头为小数点(.)时，代表这个文件是“隐藏文件”**
 
## linux 目录配置
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
   
## 目录相关操作
<br />
*所有目录下都存在两个目录"."和"..",分别代表此层目录和上次目录；同样 / 根目录也存在这两个目录，这两个目录的属性和权限完全一致，表示根目录的上层目录和根目录自己是同一个目录*

#### 几个特殊的目录
```
 .  代表此层目录
 .. 代表上层目录
 -  代表前一个工作目录
 ~  代表目前使用者身份所在的主文件夹
 ~accout 代表accout这个使用者的主文件夹
```

#### 操作指令
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

#### 环境变量 PATH
```
    echo $PATH
```
----
## 文件与目录管理  
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
| -i | 列出inode 号码 |
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

## 文件内容查阅

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
| -n | 列出

> more ： 一页一页的显示文件内容

> less ：与more类似，但less可以往前翻页

> head ： 只看头几行

> tail ： 只看尾几行

> od ： 以二进制的方式读取文件内容

 

  


