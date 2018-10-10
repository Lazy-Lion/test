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
  - 登录到系统命名行界面后如上显示,其中~表示用户的家目录；如果是root用户表示的就是/root；如果是普通用户，如personal(自建的普通用户)，表示的就是/home/personal/；#是提示字符，root用户是#,普通用户是$;

**几乎所有的硬件设备文件都在/dev目录中**

## 几个简单指令
- su - : 切换至 root
- su - username : 切换至普通用户，用户名username
- date : 显示日期，
    *例 date +%Y/%m/%d : 以年/月/日 的形式显示日期，**可以看到某些特殊情况下，选项或参数前也会带 +***
- cal :  显示日历,
    *例 cal [month] [year] ：若没有参数，则显示当前月份的日历*
- cp : 复制命令
    *cp 来源文件 目的文件* 
- shutdown :关机指令，<br />
    *例 shutdown -h now **立刻关机***<br />
    *shutdown -h 20:25  **20:25关机***<br />
    *shutdown -h +10  **10分钟后关机***<br />
    *shutdown -h +10 "system will be shutdown" **10分钟后关机,并发出警告信息***
- poweroff : 关机指令
- reboot : 重启命令
- sync : 数据同步写入磁盘，一般情况下在使用shutdown指令时，系统默认会先执行sync，也可以手动执行

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
 
 ### 权限： rwx :分别表示 可读，可写，可执行
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

### 权限相关命令
  - chgrp : 改变文件所属群组 
  - chown : 改变文件拥有者
  - chmod : 改变文件权限 ： 
    改变权限命令有多种使用方式，比较简单的是权值方式：r w x 分别使用 4 2 1 权值表示，如命令 chmod 664 .bashrc ，表示的即为 -rw-rw-r\-\-
   
     
   



  

  


