#!/usr/bin/env python3
## -*- coding: utf-8 -*-

# 第一行表示Mac,Linux下可直接执行
# 第二行表示采用utf-8编码

# sublime Text 3 默认不支持input(), 需要安装SublimeREPL插件
# ctrl + shift + p ：选择 Install Package 安装，如果无法安装参照 https://packagecontrol.io/installation
# ctrl + shift + p ：选择 sublimeREPL 安装，安装完成后Tools菜单下会出现sublimeREPL
# 设置快捷键： preferences -> key bindings : 添加如下代码
#{
#    "keys": ["f5"],
#    "caption": "SublimeREPL: Python - RUN current file",
#   "command": "run_existing_window_command",
#    "args": {
#        "id": "repl_python_run",
#        "file": "config/Python/Main.sublime-menu"
#    }
#}
# Preferences->Browse Packages 进入文件SublimeREPL->config->Python-> Main.sublime-menu 可以修改python版本
#
#


# 查看python路径
import sys
print(sys.path)

# 查看python版本 3.7
import sys
print(sys.version)

# 从cmd进入python交互：输入python
# 从python交互退回cmd：输入exit()
# windows下执行py文件，在cmd中输入 python filename.py

# python的缩进，Tab和空格不能混用

## 一、基础
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
# find()
# str(object=b'',encoding='utf-8',errors='strict'):将对象转换成其字符串表现形式
s = 'abcdef'
print(s.find('e')) # 能找到，返回index
print(s.find('m')) # 找不到，返回-1
# 布尔值： True, False ： 布尔值可以使用的运算： and, or, not
# Python中除了False,''、""、0(值为0的数都是False,如0.0)、()、[]、{}、None为False之外，其他的都是True

if not 0 : 
	print('0 is False')
if not 0.0 : 
	print('0.0 is False')
if not '' :
	print('\'\' is False')
if not "":
	print('\"\" is False')
if not ():
	print('() is False')
if not []:
	print('[] is False')
if not {}:
	print('{} is False')
if not None:
	print('None is False')
if 1:
	print('1 is True')

print('{} == False :', {} == False) # 直接比较返回False，不相等
print('0.0 == False:', 0.0 == False) # 直接比较返回True，相等


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
# 
# str：字符串
# 输出格式化字符串： % 实现： 1. %d :整数；2. %s :字符串； 3.%f :浮点数； 4.%x ：16进制整数
#     print('hi, %s,you hava $%d' % ('Michael', 10000)) 
#     格式化整数和浮点数还可以指定是否补0和整数与小数的位数 : %02d,%.2f
#     字符串中如果%表示一个普通字符，使用%%表示一个%
#     format()方法, 'hello, {0}, 成绩提升了 {1:.1f}%'.format('小明',17.125) ; {0},{1}表示占位符,format依次填充
s = 'hello world.py'
print(s.upper()) # 大写
print(s.lower()) # 小写
print(s.capitalize()) # 字符串首字母大写，其余小写
print(s.title())  # 字符串标题化，所有单词首字母大写，其余小写

# strip(): 删除字符串首尾指定的字符序列，返回新字符串 
#    strip([chars]),chars(Optional):Character or a set of characters, that needs to be removed from the string.
#                                           If no parameter is passed then only the leading and trailing spaces are removed.
#                                           空白字符除了空格还有\n等
s = '\n  abc def fed cba '
print(s)
print(s.strip())
print(s.strip('abc'))

s = 'abc def fed cba'
print(s.strip('abc')) # 返回'def fed ',删除的是参数包含的字符，不是以字符串计算的

# lstrip()
# rstrip()


#

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
s = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
  s = s + x
#      2. while
s = 0
n = 99
while n > 0:
  s = s + n
  n = n - 2



## 二、函数
# Python的函数是对象，函数可以在另一个函数内部被定义，函数可以赋值给一个变量，函数可以返回另一个函数，可以传入一个函数作为参数
# 内置函数 https://docs.python.org/3/library/functions.html
# max(),hex()
# abs():定义在builtins模块中
# sum()
# int():字符串转换成整数
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
import math
      
def move(x, y, step, angle=0):
  nx = x + step * math.cos(angle)
  ny = y - step * math.sin(angle)
  return nx, ny 
      
#      调用: x, y = move(100,100,60,math.pi/6)
#      事实上返回的是一个tuple,多个变量同时接收一个tuple，按位置赋给对应的值
#    
# 参数： 位置参数，默认参数，可变参数，关键字参数，命名关键字参数
def enroll(name, gender, age = 6, city = 'Beijing'):
  print(name)
  print(gender)
  print(age)
  print(city)
#     age,city是默认参数，调用时可以按顺序提供参数enroll('Bob','M',7);或不按顺序指定参数名enroll('Adam','M',city='Tianjin')
#     ** 默认参数必须指向不可变对象(如None,str)
def add_end(L = None):
  if L is None:
    L = []
    L.append('end')
    return L
#     如果参数直接使用 L = [],多次调用add_end()会产生错误

def calc(*numbers):
  s = 0
  for n in numbers:
    s = s + n
  return s
#     *numbers表示可变参数(0个或多个)，函数内部numbers是自动组装成的tuple(note:tuple指向不可变)
#     Python允许在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去
#     调用：
calc()
calc(1,2)
nums = [1,2,3]  
calc(*nums)
#################################    
def person(name,age,**kw):
  print('name:',name,'age:',age,'other:',kw)

#     **kw表示关键字参数(0个或多个含参数名的参数)，关键字参数在函数内部自动组装成一个dict
#     **extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra
#     调用：
person('Michael',30) # 输出：name: Michael age: 30 other: {}
person('Adam',45,gender='M',job='Engineer') # 输出： name: Adam age: 45 other: {'gender': 'M', 'job': 'Engineer'}
#####
def person(name,age,*,city,job):
  print(name,age,city,job)
#     命名关键字参数，上述定义表示只接收city,job作为关键字参数，*表示的是分割符，如果函数定义已经有一个可变参数，后面跟着的命名关键字参数就不需要*分割符
#     命名关键字参数必须传入参数名，有默认值的命名关键字参数可以不传值
def person(name,age,*args,city,job):
  print(name,age,args,city,job)
  
def person(name,age,*args,city='shanghai',job):
  print(name,age,args,city,job)

# 递归函数:使用递归函数需要注意防止栈溢出。在计算机中，函数调用是通过栈（stack）实现的，每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧
# 尾递归：在函数返回的时候，调用函数自身，并且return语句不能包含表达式
# python 解释器对尾递归没有优化，尾递归依然会导致栈溢出

def fact(n):
  if n == 1: 
    return 1
  return n * fact(n - 1)

print(fact(5))

def fact_iter(n, result):
  if n == 1:
    return result
  return fact_iter(n - 1, n * result)

print(fact_iter(5, 1))

# 汉罗塔：n表示3个柱子中第1个柱子的盘子数量，然后打印出把所有盘子从a借助b移动到c的方法
def move(n,a,b,c):
  if n == 1: 
    print(a, '-->', c)
  else:
    move(n-1,a,c,b)
    print(a, '-->', c)
    move(n-1,b,a,c)

move(3,'A','B','C')

## 三、高级特性
# 切片： 取list、tuple的部分元素；str也可以进行切片，返回str
L = list(range(0,11))
print(L)
print(L[0:3])  # 取前3个，索引 [0,3) ,左闭右开
print(L[:3])   # 缺省值为0
print(L[1:3])  # [1,3)
print(L[-2:])  # 后两个，缺省值为len(L)
print(L[1:])
print(L[:])    # 原样复制
print(L[::2])  # 对整个list，每2个取一个，第一个L[0]取
print(L[1:7:2])

# L[i:j:s]: s 缺省是1，表示步进；
#           s < 0 时，i缺省时默认为-1，j缺省时默认为-len(L)-1
print(L[::-1]) # 同L[-1:-len(L)-1:-1],列表倒序
print(L[-1:-len(L)-1:-1])



# 去除字符串首尾空格
def trim(s):
  while s and s[0] == ' ':
    s = s[1:]
  while s and s[-1] == ' ':
    s = s[:-1]
  return s

# 迭代：给定一个list或tuple,可以通过for遍历这个list或tuple，这种遍历成为迭代(Iteration)
# python中的可迭代对象(Iterable)： list,tuple,dict(默认情况下dict迭代的是key，for value in d.values() 迭代value,
#     for k,v in d.items() 同时迭代key和value), str 等
for c in 'ABC':
  print(c)  
# 判断可迭代对象：
from _collections_abc import Iterable    # from collections import Iterable 的替代，该方式Deprecated 
print(isinstance('abc',Iterable))

# enumerate()： 把list变成索引(下标)-元素对
for i,value in enumerate(['a','b','c']):
	print(i,value) 

# list中的最小值和最大值
def findMinAndMax(L):        # 迭代方式
	if L == None or L == []:
		return (None, None)
	else : 
		min = max = L[0]
		for x in L:
			if min > x:
				min = x
			if max < x:
				max = x
		return (min,max)


def findMinAndMax(L):
	if(len(L) > 0):
		return (min(L), max(L))
	return (None,None)



# 列表生成式(List Comprehensions)：用来创建list的生成式
print(list(range(1,11)))
print([x*x for x in range(1,11)])   # 列表生成式: 要生成的元素x * x放到前面，后面跟for循环
print([x*x for x in range(1,11) if x % 2 == 0])
print([m + n for m in 'ABC' for n in 'XYZ'])

import os 
print([d for d in os.listdir('.')])  # 列出当前目录下的所有文件和目录名

L = ['Hello','World','IBM','Apple']
print([s.lower() for s in L])

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s,str)]  # 字符串小写
print(L2)

# 生成器(generator):边循环边计算，也是可迭代对象
# 创建方式1：列表生成式的[]改为()
g = (x*x for x in range(1,11))
print(g)
print(next(g)) # next()获得generator的下一个返回值,没有更多元素时抛出StopIteration错误

print("for 迭代")
for x in g:
	print(x)
print("第二次迭代,没有数据返回")
for x in g:
	print(x)

# 创建方式2：函数方式,如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
#        调用方式：每次调用next()时执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行,也就是说每次调用都默认一致上次调用的返回值
def fib(max):
	n,a,b = 0,0,1
	while n < max:
	  yield b # print(b)
	  a,b = b, a+b  # note: 与a=b b=a+b 不同，相当于tuple = (b, a + b) a=tuple[0] b=tuple[1]
	  n = n + 1
	return 'done' 

g = fib(5)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

print('##############')

for x in fib(6):
	print(x)


g=fib(6)
while True:  
	try:
		print('g:', next(g))
	except StopIteration as e:    # 获取generator的return返回值
		print('Generator return value:', e.value)
		break

# zip()函数将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表(在 Python 3.x 中为了减少内存，zip()返回的是一个对象。如需展示列表，需手动 list() 转换)。
# zip([iterable, ...])
L = ['a','b','c','d','e','f']

print(list(zip(L[:-1],L[1:])))

L = ['flower','flow','flight']
print(list(zip(*L)))

# 杨辉三角：每一行看做一个list
def triangles():
	a = [1]
	while 1:
		yield a 
		a = [ x+y for x,y in zip([0]+a,a+[0])]

g=triangles()

def getTriangles(g):
	n = 0
	while n < 10:
		print(next(g))
		n = n + 1

getTriangles(g)


# 迭代器：可以直接作用于for循环的对象统称为可迭代对象(Iterable)
#        生成器generator不仅可以使用for迭代，还可以被next()函数不断调用返回下一个值，直到抛出StopIteration
#        可以被next()调用并不断返回下一个值的对象成为迭代器(Iterator)
#        生成器既是Iterable,也是Iterator; list、str、dict等是Iterable,但不是Iterator
#    Iterable:可迭代对象； Iterator：迭代器
# iter():把Iterable变成Iterator
# Iterator表示一个惰性计算的序列，只有在需要返回下一个数据时(调用next())它才会计算
# Iterator甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的。
# Python的for循环本质上是通过不断调用next()函数实现的

from _collections_abc import Iterable,Iterator
print(isinstance('abc',Iterable))   # True
print(isinstance('abc',Iterator))   # False
print(isinstance(triangles(),Iterable)) # True
print(isinstance(triangles(),Iterator)) # True
print(isinstance(iter('abc'),Iterator)) # True


## 四、函数式编程 Functional Programming
# 1.变量可以指向函数
# 2.函数名也是变量,abs=10 就会把abs指向整数10，而不指向求绝对值函数，也就无法调用abs(-10)
# 3.高阶函数：接收另一个函数作为参数
print(abs)  # 输出的是函数本身，<built-in function abs>
a = abs
print(a(-10))


def add(x,y,f):
	return f(x) + f(y)

print(add(-5,6,abs))

# 关于map/reduce的概念：https://ai.google/research/pubs/pub62
# map()：map()接收两个参数，一个是函数，一个是Iterable,map将传入的函数依次作用到序列的每一个元素，并把结果作为新的Iterator返回

def f(x):
	return x * x 
r = map(f,[1,2,3,4,5,6,7,8,9])
print(list(r))

# reduce():把一个函数作用在一个序列[x1,x2,x3,...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累计计算
#   reduce(f,[x1,x2,x3,x4]) = f(f(f(x1,x2),x3),x4)
from functools import reduce 
def add(x,y):
	return x + y 
print(reduce(add, range(1,101))) # 与调用sum(range(1,101))效果一致

def fn(x,y):
	return 10*x + y 
print(reduce(fn,[1,3,5,7,9]))
 
# lambda表达式： lambda 参数:操作(参数)
print(reduce(lambda x,y : 10*x+y, [1,3,5,7,9]))


# 1.输入英文名首字母大写，其他字母小写
def normalize(s):
	if len(s) > 0 :
		s = s[0].upper() + s[1:].lower()
		return s
	return None


L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

# 2.list求积
def fn(x,y):
	return x*y 

def prod(L):
	return reduce(fn, L)


print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')


# 3.字符串转换成浮点数
def str2float(s):
	nums = {'0': 0,'1': 1,'2': 2,'3': 3,'4': 4,'5': 5,'6': 6,'7': 7,'8': 8,'9': 9}
	def char2digit(c):
		return nums[c]

	p = s.find('.')
	l,r = s[:],''
	ls,rs = 0,0
	if p >= 0:
	 r = s[p+1 :]
	 l = s[:p]
	 rs = reduce(lambda x,y : x * 0.1 + y,map(char2digit,reversed(r))) * 0.1
	ls = reduce(lambda x,y : 10 * x + y,map(char2digit,l))
	return ls + rs



print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')

print(str2float('23213'))


# filter():接收一个函数和一个序列，把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
#          返回的是Iterator
def not_empty(s):
	return s and s.strip()

print(list(filter(not_empty,['a','b','c','',' ',None])))


# 求素数:
# 素数： 在大于1的自然数中，除了1和它本身以外不再有其他因数。
# 解法：埃氏筛法
def odd_iter():  # 大于1的奇数序列
	n = 1
	while 1:
		n = n + 2 
		yield n 

def not_divisible(n): 
	return lambda x : x % n > 0 

def primes():
	yield 2 
	it = odd_iter()
	while 1 : 
		n = next(it)
		yield n 
		it = filter(not_divisible(n),it)

#      打印100以内的素数:
for n in primes():
    if n < 100:
        print(n)
    else:
        break

# 判断回数
def is_palindrome(n):
	return str(n) == str(n)[::-1]

output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')


# sorted():高阶函数，对list进行排序
print(sorted([1,3,2,7,5,6]))
print(sorted([1,3,-2,-7,5,6],key = abs))  # 自定义排序方式，按绝对值大小排序,key函数作用于每个元素
print(sorted(['bob','about','Zoo','Credit']))
print(sorted(['bob','about','Zoo','Credit'],key = str.lower))
print(sorted(['bob','about','Zoo','Credit'],key = str.lower,reverse = True)) # 反向排序


L = [('Bob',75), ('Adam',92), ('Bart',66), ('Lisa',88)]
def by_name(t):  #按名字排序
	name,score = t 
	return name

def by_score(t):  #按成绩从高到低排序
	name,score = t 
	return score 

print(sorted(L,key = by_name))
print(sorted(L,key = by_score, reverse = True))

# 返回函数：内部函数可以引用外部函数的参数和局部变量，当外部函数返回内部函数时，相关参数和变量都保存在返回的函数中，即"闭包"
#         lazy_sum每次调用返回的都是新的函数，即使传入相同的参数；返回的函数并没有立刻执行，而是直到调用了f()才执行
#   (闭包(Closure)：在计算机科学中，闭包（英语：Closure），又称词法闭包（Lexical Closure）或函数闭包（function closures），
#                   是引用了自由变量的函数。这个被引用的自由变量将和这个函数一同存在，即使已经离开了创造它的环境也不例外。 )
#   内部函数只能引用而不能修改外部函数中定义的自由变量
#   <https://stackoverflow.com/questions/111102/how-do-javascript-closures-work>
def lazy_sum(*args):
	def csum():
		ax = 0
		for n in args:
			ax = ax + n 
		return ax 
	return csum
f = lazy_sum(*list(range(1,11)))
print(f)
print(f())


def count():
	fs = []
	for i in range(1,4):
		def f():
			return i * i
		fs.append(f)
	return fs

f1,f2,f3 = count()
print(f1(), f2(), f3())  # 返回值都是9，即返回的函数直到调用时才执行

# 返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。

# 如果一定要引用循环变量：再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变
def count():
	def f(j):
		def g():
			return j * j
		return g
	fs = []
	for i in range(1,4):
		fs.append(f(i))
	return fs 

def count():  # 使用lambda简化上述代码
	fs = []
	for i in range(1,4):
		fs.append((lambda j : lambda : j * j)(i))
	return fs

f1,f2,f3 = count()
print(f1(),f2(),f3())

f1,f2,f3 = [(lambda j : lambda : j * j)(i) for i in range(1,4)] # 使用列表生成式简化上述代码
print(f1(),f2(),f3())


# 计数器函数，递增整数 （生成器方式）
def createCounter():
	def g():
		v = 1
		while 1 :
			yield v 
			v = v + 1 

	count = g()
	def counter():
#		count = count + 1  # 不能直接修改外部变量的值
		return next(count) 
	return counter

# 计数器函数，递增函数 (全局变量方式)
def createCounter():
	global count 
	count = 0 
	def counter():
		global count
		count += 1
		return count
	return counter  


# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')


# 匿名函数：lambda表达式
#   限制：只能有一个表达式，不用写return，返回值就是该表达式的结果,冒号前面表示函数的参数
print(list(map(lambda x : x*x, range(1,11))))
print(list(filter(lambda n : n % 2 == 1, range(1,20))))

# 装饰器(Decorator)：在代码运行期间动态增加功能的方式；允许在被装饰函数前后执行代码，而不对函数本身做任何修改
#          本质上，decorator就是一个返回函数的高阶函数
# <http://kissg.me/2016/07/16/translation-about-python-decorator/>
def now():
	print('2018-11-19')
f = now
f()
print(f.__name__)  # 函数对象有一个__name__属性


def log(func):
	def wrapper(*args, **kw):  
		print('call %s():'% func.__name__)
		return func(*args, **kw) # 调用原始函数
	return wrapper

@log  # Python的@语法，将decorator置于函数的定义处,相当于log(now)，一个函数可以使用多个装饰器，按照书写顺序执行
def now():
	print('2018-11-19')

now()
print(now.__name__) # 函数名变成了wrapper

# 如果装饰器本身需要传入参数
def log(text):
	def decorator(func):
		def wrapper(*args, **kw):
			print('%s %s():' % (text,func.__name__))
			return func(*args, **kw)
		return wrapper
	return decorator

@log('execute') # 效果相当于log('execute')(now)
def now():
	print('2018-11-19')

now()
print(now.__name__) # 函数名变成了wrapper


# 装饰器返回的函数名变更，需要把原始函数的__name__等属性复制到wrapper()函数中，否则有些依赖函数签名的代码执行就会出错
import functools

def log(func):
	@functools.wraps(func)  # 用于将原始函数的一些属性复制到wrapper()函数中
	def wrapper(*args, **kw):
		print('call %s()' % func.__name__)
		return func(*args, **kw)
	return wrapper

@log
def now():
	print('2018-11-19')

print(now.__name__)


# 装饰器模式：打印函数执行时间
import time,functools

def metric(func):
	@functools.wraps(func)
	def wrapper(*args, **kw):
		start = time.perf_counter()
		func(*args, **kw)
		end = time.perf_counter()
		print('%s excuted in %s ms ' % (func.__name__, end - start))
		return func(*args, **kw)
	return wrapper

@metric 
def func():
	for x in range(1,100):
		pass
func()

# 装饰器既支持@log，也支持@log('execute')的写法
def log(func):
	if callable(func):
		@functools.wraps(func)
		def wrapper(*args, **kw):
			print('call %s:' % func.__name__)
			return func(*args, **kw)
		return wrapper
	else: 
		def decorator(fn):
			@functools.wraps(fn)
			def wrapper(*args, **kw):
				print('%s %s' % (func, fn.__name__))
				return fn(*args, **kw)
			return wrapper
		return decorator

@log
def now():
	print('2018-11-19')
now()
print(now.__name__)

@log('execute')
def now():
	print('2018-11-19')
now()
print(now.__name__)
print('------')
origin_now = now.__wrapped__  # python 3 中使用该属性可以调用去decorator的函数
origin_now()

# 偏函数(Partial function): functools.partial() 创建一个偏函数,参数为：函数对象,*args,**kw
print(int('12345'))
print(int('1001101',base = 2))

def int2(x,base = 2):
	return int(x,base)

print(int2('1001101'))

import functools
int2 = functools.partial(int, base = 2)  # functools.partial创建一个偏函数，也就是对函数的某些参数设置默认值，返回新的函数; 相当于functools.partial(int, **{'base':2})
print(int2('1001101'))
print(int2('123',base = 10))  # 有默认值的参数同样可以传入新值

int2 = functools.partial(int, **{'base':2})
print(int2('1001101'))

max2 = functools.partial(max, 10) 
print(max2(5,6,7)) # 相当于max(*(10,5,6,7)),即当成*args的一部分自动加到左边


## 五、模块：在Python中一个.py文件就称为一个模块(Module). 相同名字的函数和变量完全可以分别存在于不同的模块中.但尽量不要与内置函数名冲突.
#自己创建模块时要注意命名，不能和Python自带的模块名称冲突。例如，系统自带了sys模块，自己的模块就不可命名为sys.py，否则将无法导入系统自带的sys模块.
#  可以在命名前检查系统是否已存在该模块，在交互环境下执行import modulename ，若成功则表明已存在。

# 为了避免模块名冲突，Python引入按目录来组织模块的方法，称为包(Package). 每一个包目录下都会有一个__init__.py文件，必须存在。
#  mycompany
#  ├─ __init__.py
#  ├─ abc.py
#  └─ xyz.py
# 上述示例： mycompany是包名，__init__.py对应的模块名就是mycompany，abc.py对应的模块名是mycompany.abc

# 如下多级目录结构：www.py的模块名是mycompany.web.www
#  mycompany
#   ├─ web
#   │  ├─ __init__.py
#   │  ├─ utils.py
#   │  └─ www.py
#   ├─ __init__.py
#   ├─ abc.py
#   └─ xyz.py

# 模块代码示例:hello.py


#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'Michael Liao'

import sys

def test():
    args = sys.argv
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

if __name__=='__main__':
    test()

# 上述代码：第1、2行是标准注释；第4行是一个字符串，表示模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释；
# 		   第6行使用__author__变量把作者写进去； 后面是正式代码
#     sys.argv变量用list存储命令行的所有参数,argv至少有一个元素，第一个参数永远是运行的.py文件名称：
#			python hello.py  的sys.argv为['hello.py']
# 			python hello.py Michael  的sys.argv为['hello.py','Michael']
#     命令行执行hello.py时，python解释器将特殊变量 __name__ 置为 __main__ ，而当导入时则不会设置，因此导入时不会自动运行test()，需手动调用hello.test()，因此可以用于运行测试。


# 作用域：
#        1.public：正常的函数和变量名是公开的，可以被外部直接引用，如 a,b1
#		 2.特殊变量：__xxx__ ,可以被外部直接引用，但是有特殊用途，如 __name__ ,我们自己的变量一般不要用这种变量名
#        3.private：_xxx, 不应该被外部直接引用(Python并没有一种方法可以可以完全限制访问private函数或变量，但是从编程习惯上不应该引用private函数或变量)


# 安装第三方模块：通过包管理工具pip完成
# 一般来说，第三方库都会在Python官方的 https://pypi.org/ 网站注册
# 例： pip install Pillow     # 命令行模式下输入，安装Pillow库
# Anaconda: https://www.anaconda.com/  

# 模块搜索路径：当我们试图加载一个模块时，Python会在指定路径下搜索对应的.py文件，如果找不到则报错；
#              默认情况下Python解释器会搜索当前目录、所有已安装的内置模块和第三方模块，搜索路径存放在sys模块的path变量中;
#			   如果要添加自己的搜索目录： 1.修改sys.path：sys.path.append('E:\\my_py_scripts'),运行时修改，运行结束后失效；   2.设置环境变量PYTHONPATH,该环境变量内容自动加到模块搜索路径中

import sys
print(sys.path)


## 六、面向对象编程 Object Oriented Programming：封装、继承、多态
# 在Python中所有数据类型都可以视为对象

class Student(object):  #类定义，类名为Student，(object)表示该类继承自object类(所有的类最终都会继承的类，没有合适的继承类时就用object类)

	def __init__(self, name, score):  #__init__方法(类似于构造方法)的第一个参数永远是self，表示创建的实例本身
		self.name = name
		self.score = score

	def print_score(self):            # 类中定义的函数第一个参数永远是实例变量self，调用时不用传递该参数，其他与普通函数相同
		print('%s: %s' % (self.name,self.score))

print(Student)
lisa = Student('Lisa Simpson', 87)  # 实例对象
print(lisa)
lisa.print_score()
lisa.score = 95     # 可以外部访问属性
lisa.print_score()

lisa.age = 10     # Python允许对实例变量任意绑定属性，也就是说对于两个实例变量，即使是同一个类的不同实例，拥有的变量名称都可能不同
print(lisa.age)

class Student(object):

	def __init__(self, name, score):
		self.__name = name
		self.__score = score

	def get_name(self):
		return self.__name

	def get_score(self):
		return self.__score

	def set_name(self, name):
		self.__name = name

	def set_score(self, score):
		if 0 <= score <= 100:
			self.__score = score
		else :
			raise ValueError('bad score')

	def print_score(self):
		print('%s: %s' % (self.name,self.score))

lisa = Student('Lisa Simpson', 87)
# print(lisa.__score)  # 在Python中，实例的变量名以两个下划线__开头，就变成一个私有变量(private)，只能内部访问，外部无法访问(以双下划线开头并且以双下划线结尾的是特殊变量，可以直接访问，不是private)
				       #            以一个下划线开头的实例变量名，外部是可以访问的，但是按照约定俗成的规定，"虽然我可以被访问，但是，请把我视为私有变量，不要随意访问"
				       #			双下划线的实例变量不能直接访问是因为Python解释器对外把__score变量改为_Student__score，所以仍然可以通过_Student__score来访问(不同版本解释器可能会改成不同的变量名)

print(lisa._Student__score)
print(lisa.get_score())

lisa.__name = 'new name'   # 实际上是新增了一个__name变量，而不是修改实例内部的__name变量
print(lisa.get_name())


# 继承 :
class Animal(object):
	def run(self):
		print('Animal is running...')

class Dog(Animal):
	def run(self):  # 重写
		print('Dog is running')

dog = Dog()
dog.run()

def run_func(animal):
	animal.run()    # 实际上，对于动态语言来说，传入的对象有run()方法即可，不一定要是Animal或其子类型 ("鸭子类型")

run_func(Dog())
run_func(Animal())


# type():判断对象类型
print(type(123)) 
print(type(None))
print(type(str))
print(type('str'))
print(type(abs))
print(type(dog))

# 判断基本数据类型
print('test primary type:')
print(type(123) == int)
print(type('123') == str)
print(type([1]) == list)

# 判断对象是否为函数，types模块
print('test types module:')
import types

def fn():
	pass

print(type(fn) == types.FunctionType)
print(type(lambda x : x * x) == types.LambdaType)
print(type(abs) == types.BuiltinFunctionType)
print(type((x for x in range(100))) == types.GeneratorType)

# 判断class的类型, 使用isinstance()
print('test isinstance():')
print(isinstance(dog, Animal))
print(isinstance(Animal(), Animal))
print(isinstance('str', str))  # 能用type判断的，也能使用isinstance()判断，优先使用isinstance()判断
print(isinstance(b'123', bytes))

# dir() :获得一个对象的所有属性和方法
print(dir('str'))
print(dir(dog))

# len('ABC') <=> 'ABC'.__len__()

print(len('ABC'))  # len()函数实际上自动调用对象的__len__()方法
print('ABC'.__len__())


class MyDog(object):
	def __init__(self, x, y):
		self.__x = x
		self.y = y

	def __len__(self):
		return 100

dog = MyDog('x','y')
print(len(dog))

print(dir(dog))

# getattr()、setattr()、hasattr() 可用于对象的属性或方法 
print(hasattr(dog, '__x')) #  无法访问private属性,返回False
print(hasattr(dog,'y'))
print(setattr(dog, 'y', 'name'))
print(getattr(dog, 'y'))
print(getattr(dog, 'z', 404)) # 可以传入一个默认参数，如果属性不存在，就返回默认值

# 类属性: 实例属性属于各个实例所有，互不干扰；类属性属于类所有，所有实例共享一个属性
class Student(object):
	name = 'class value'


s = Student()
print(s.name)
print(Student.name)
s.name = 'instance value'
print(s.name)  # 实例属性优先级比类属性高，返回 instance value
print(Student.name) # 类属性并未消失，返回 class value


## 七、面向对象高级编程：多重继承、定制类、元类

# 给实例绑定属性和方法
class Student(object):
	pass

s = Student()
s.name = 'Michael' # 给实例绑定属性
print(s.name)

def set_age(self, age):
	self.age = age

from types import MethodType
s.set_age = MethodType(set_age, s) # 给实例绑定方法，对其他实例不起作用
s.set_age(5)
print(s.age)

def set_score(self, score):
	self.score = score

Student.set_score = set_score # 给类绑定方法，对所有实例有效
s.set_score(90)
print(s.score)

Student.gender = 'male' # 给类绑定属性

class Student(object):
	__slots__ = ('name', 'age') #限制实例能添加的属性，仅对当前类实例有效，对子类实例无效，对类也无效

s = Student()
s.name = 'lisa'
s.age = 10
# s.score = 90  实例无法绑定score , AttributeError
Student.score = 90  # 类依然可以绑定

class HighStudent(Student):
	pass

s = HighStudent()
s.score = 90 # 子类可以绑定


# @property: 内置装饰器负责把一个方法变成属性调用
class Student(object):

	@property       # getter方法变为属性，同时创建了另一个装饰器@score.setter
	def score(self):
		return self._score
	
	@score.setter  # setter方法变为属性赋值，如果只设置@property表示该属性只读
	def score(self, score):
		if not isinstance(score, int):
			raise ValueError('score must be an integer')
		if score < 0 or score > 100:
			raise ValueError('score must between 0 ~ 100')
		self._score = score

print('test @property:')
s = Student()
s.score = 100
print(s.score)
# s.score = 120  # 根据数据验证，ValueError


class Screen(object):

	@property
	def width(self):
		return self._width
	
	@width.setter
	def width(self, width):
		self._width = width

	@property
	def height(self):
		return self._height
	
	@height.setter
	def height(self, height):
		self._height = height

	@property
	def resolution(self):
		return 786432

s = Screen()
s.width = 1024
s.height = 768

# 多重继承: MixIn的设计
#        关于多重继承方法的调用顺序(MRO)：https://kevinguo.me/2018/01/19/python-topological-sorting/
class Animal(object):
	pass

class Runnable(object):
	def run(self):
		print('running...')

class Dog(Animal, Runnable):
	pass


# 定制类： 
# __str__(), __repr__()  ---> toString()
print('定制类：')

class Student(object):
	def __init__(self, name):
		self.name = name
print(Student('Michael'))

class Student(object):
	def __init__(self, name):
		self.name = name
	def __str__(self):
		return 'Student object (name: %s)' % self.name
print(Student('Michael'))

class Student(object):
	def __init__(self, name):
		self.name = name
	def __str__(self):
		return 'Student object (name: %s)' % self.name

	__repr__ = __str__   # 为开发者调试服务的，在python交互界面，不用print，直接敲变量时会执行



#  __iter__(), __next__()  ---> 迭代对象
class Fib(object):
	def __init__(self):
		self.a, self.b = 0, 1
	def __iter__(self):
		return self
	def __next__(self):
		self.a, self.b = self.b, self.a + self.b 
		if self.a > 10000:
			raise StopIteration()
		return self.a

for v in Fib():
	print(v)
print('##########')

# __getitem__()  ---> 下标获取， 对应的还有__setitem__(),__delitem__()，使得自定义的类表现的和list、tuple、dic等一致
class Fib(object):
	def __getitem__(self, n):
		a,b = 1,1
		for x in range(n):
			a,b = b,a+b
		return a
print(Fib()[10])

#  实现slice的部分功能
class Fib(object):
	def __getitem__(self, n):
		if isinstance(n, int):
			a,b = 1,1
			for x in range(n):
				a,b = b, a+b
			return a
		if isinstance(n, slice):
			start = n.start
			stop = n.stop

			if start is None:
				start = 0
			a,b = 1,1

			L = []
			for x in range(stop):
				if x >= start:
					L.append(a)
				a,b = b, a+b 
			return L
print(Fib()[:10])

# print('中文输出正常')  # 文件开始指定utf-8编码
# print('hello word')
# print(100+200)
# print('the quick brown fox','jumps over','the lazy dog.')
# print('100+200')
# print('1024 * 768 = ',1024 * 768)

# name = input()
# print('hello', name)

# name = input('please enter you name: ')
# print('hello', name)


# a = -100
# if a >= 0:
# 	print(a)
# else:
# 	print(-a)

# # 多行内容表示
# print('''line1
# line2
# line3''')

# # 在python 交互环境下，第一行后每行会自动生成... ,文本编辑下不用加
# # print('''line1
# # ... line2
# # ... line3''')

# print(r'''hello, \n
# world''')

# print('''hello, \n
# world''')

# print('True and False:',True and False,'\n','True or False:',True or False,'\n','not True:',not True)

# n = 123
# f = 456.789
# s1 = 'Hello, world'
# s2 = 'Hello, \'Adam\''
# s3 = r'Hello, "Bart"'
# s4 = r'''Hello,
# Lisa!'''
# print(n)
# print(f)
# print(s1)
# print(s2)
# print(s3)
# print(s4)

# # print('A'), 0041是A的unicode编码
# print('\u0041')

# # 格式化输出字符串, %
# print('hi, %s,you hava $%d' % ('Michael', 10000)) 
# # 单个，可以省略()
# print('hi, %s' % 'Michael')
