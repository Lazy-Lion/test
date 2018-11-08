#!/usr/bin/env python3
## -*- coding: utf-8 -*-

## 基础
# 编码问题： 在计算机内存中，统一使用Unicode编码，当需要保存到硬盘或者需要传输的时候，就转换为UTF-8编码。
# Python 是大小写敏感的
# 整数：十六进制使用 0x 前缀
# 浮点数：1.2 * 10^9 表示为 1.2e9
# Python的整数没有大小限制，而某些语言的整数根据其存储长度是有大小限制的，例如Java对32位整数的范围限制在-2147483648-2147483647。
# Python的浮点数也没有大小限制，但是超出一定范围就直接表示为inf（无限大）。
# 字符串：使用单引号'或双引号"括起来的任意文本，如果字符串中包含单引号或双引号，使用\转义
#        r''表示引号内部的字符串默认不转义;  使用'''括起来可以表示多行内容，而不必使用\n
#        a = 'abc'
#        a.replace('a','A') ==> 'Abc',此时print(a) 依然是'abc', str是不可变对象
# 布尔值： True, False ： 布尔值可以使用的运算： and, or, not
# 
# input() 输入： 返回的数据类型是str, int()函数将str转换成整数
#     s = input()
#     s = int(s)    
# print() 输出
# 
# 空值： None
# 变量： 字母，数字，下划线组成，开头不能是数字；同一个变量可以反复赋值，而且可以是不同的类型(动态语言)
# 运算： /  ： 除法，结果是浮点数，即使整数恰好整除，结果也是浮点数；
#       // ： 地板除，只取结果的整数部分
#       %  ： 取余
# a = 'ABC' : Python 解释器操作： 1.在内存中创建了一个'ABC'的字符串；2.在内存中创建了一个名为a的变量，并把它指向'ABC'。
# 变量赋值 x = y : 把变量x指向真正的对象，该对象是变量y所指向的。
# ord() ： 获取字符的整数表示,Unicode 字符集： ord('A') ==> 65
# chr() ： 把编码转换成对应的字符： chr(65) -> 'A'
# encode()：以unicode表示的str类型数据通过encode()方法编码为指定的bytes类型数据(以b为前缀), 例： 'ABC'.encode('ascii')  ==> b'ABC'(前缀为b表示bytes类型的数据，每个字符都只占用一个字节，在bytes中，无法显示为ASCII字符的字节，用\x##显示。)
# decode()：bytes->str,例： b'ABC'.decode('ascii') ==> 'ABC'
# encode(),decode() 方法对于无法正确编码或解码的会报错；对于decode(),如果bytes中只有一小部分无效的字节，可以传入errors='ignore'忽略错误的字节：b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore')
# len() : 计算str包含多少字符: len('中文A') ==> 3；对于len(b'ABC') ==> 3,计算的就是字节数 
# 输出格式化字符串： % 实现： 1. %d :整数；2. %s :字符串； 3.%f :浮点数； 4.%x ：16进制整数
#     print('hi, %s,you hava $%d' % ('Michael', 10000)) 
#     格式化整数和浮点数还可以指定是否补0和整数与小数的位数 : %02d,%.2f
#     字符串中如果%表示一个普通字符，使用%%表示一个%
#     format()方法, 'hello, {0}, 成绩提升了 {1:.1f}%'.format('小明',17.125) ; {0},{1}表示占位符,format依次填充
# list : 内置的数据类型，有序集合，可以随时添加和删除其中的元素，list里元素的数据类型可以不同
#     classmates = ['Michael', 'Bob', 'Tracy']
#     len(classmates) ==> 3
#     可以使用索引访问, classmates[0] ==> Michael
#     访问最后一个数据，还可以使用 classmates[-1],依此类推 -2 表示倒数第二个数据
#     classmates.append('Adam') ==> list追加元素到末尾
#     classmates.insert(1,'Jack') ==> 元素插入指定的 1 位置
#     classmates.pop() ==> 删除list末尾元素
#     classmates.pop(1) ==> 删除list指定的 1 位置元素
#     classmates[1] = 'Sarah' ==> 替换元素值
#     classmates.sort()  ==> 排序
#     s = ['python', 'java', ['asp', 'php'], 'scheme'] ==> len(s) == 4 ,s[2][1] == 'asp'
#     L = [] ==> len(L) == 0
#    
# tuple: 元组，有序列表，初始化之后不能修改。
#     可变tuple：所谓不变是指元素的指向不变，如果某个tuple中有个元素是list，可以修改list里的元素值。
#     classmates = ('Michael', 'Bob', 'Tracy') 
#     ** 对于定义只有一个元素的tuple时，应该写成 t = (1,);  t = (1) 等价于 t = 1
# dict: 字典，键值对存储(key-value)
#     dic的key必须是不可变对象
#     d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
#     d['Michael']  ==> 95
#     d['Jack'] = 90 ==> 如果key已存在，会重新设值；若key不存在，字典新增键值对
#     'Thomas' in d ==> 判断key是否存在，返回True/False
#     d.get('Thomas') ==> key不存在返回None(返回None的时候Python的交互环境不显示结果),存在时返回value
#     d.get('Thomas', -1) ==> key不存在返回-1,存在时返回value
#     d.pop('Jack') ==>删除key和对应的value
# set: key的集合，无序、不重复； set原理和dict一样，不可以放入可变对象
#     创建set需要提供一个list作为输入集合  
#     s = set([1,2,2,3,4]) ==> {1,2,3,4} 
#     s.add(key) ==>  添加元素
#     s.remove(key) ==> 删除元素
#     s1 & s2 ==> 两个set交集
#     s1 | s2 ==> 两个set并集
#     
#     
#     
# 条件判断： 
#     if condition1:
#         statement1
#     elif condition2:
#         statement2
#     else:
#         statement3
# 
#     对于非布尔类型的条件： 非零数值，非空字符串，非空list等判断为True;否则为False
# 
# range()：生成一个整数序列,range(5) ==> 序列为从0开始小于5的整数
# list() ： 将序列转换成list, list(range(5)) ==> [0,1,2,3,4]
# 
# 循环： 语句块的编写需要缩进， 循环中的break,continue和java用法一致
#     Ctrl + C ： 强制退出程序
#     1. for ... in ...
#     sum = 0
      for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
          sum = sum + x
      2. while
      sum = 0
      n = 99
      while n > 0:
          sum = sum + n
          n = n - 2



## 函数
# 内置函数 https://docs.python.org/3/library/functions.html
# max(),abs(),int(),hex()
# 函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”:
#     a = abs
#     a(-10)  ==> 10
# 函数定义def
#     def my_abs(x):
#         if x >= 0:
#             return x
#         else:
#             return -x
# 如果函数没有return,函数执行完毕后也会有返回，返回结果为None. return None可简写为return
# 空函数： pass语句什么也不做，用作占位符
#     def nop():
#         pass   
# 参数检查： 参数个数不对，python解释器会自动检查，并抛出TypeError
#           参数类型不对，python解释器无法帮我们检查，需要手动检查
#     def my_abs(x):
#         if not isinstance(x, (int, float)):
#             raise TypeError('bad operand type')
#         if x >= 0:
#             return x
#         else:
#             return -x
# 返回多个值：
#      import math
#      
#      def move(x, y, step, angle=0):
#          nx = x + step * math.cos(angle)
#          ny = y - step * math.sin(angle)
#          return nx, ny 
#      
#      调用: x, y = move(100,100,60,math.pi/6)
#      事实上返回的是一个tuple,多个变量同时接收一个tuple，按位置赋给对应的值
#           

print('中文输出正常')
print('hello word')
print(100+200)
print('the quick brown fox','jumps over','the lazy dog.')
print('100+200')
print('1024 * 768 = ',1024 * 768)

name = input()
print('hello', name)

name = input('please enter you name: ')
print('hello', name)


a = -100
if a >= 0:
	print(a)
else:
	print(-a)

# 多行内容表示
print('''line1
line2
line3''')

# 在python 交互环境下，第一行后每行会自动生成... ,文本编辑下不用加
# print('''line1
# ... line2
# ... line3''')

print(r'''hello, \n
world''')

print('True and False:',True and False,'\n','True or False:',True or False,'\n','not True:',not True)

n = 123
f = 456.789
s1 = 'Hello, world'
s2 = 'Hello, \'Adam\''
s3 = r'Hello, "Bart"'
s4 = r'''Hello,
Lisa!'''
print(n)
print(f)
print(s1)
print(s2)
print(s3)
print(s4)

# print('A'), 0041是A的unicode编码
print('\u0041')

# 格式化输出字符串, %
print('hi, %s,you hava $%d' % ('Michael', 10000)) 
# 单个，可以省略()
print('hi, %s' % 'Michael')