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


# 全局变量(global variable)和局部变量(local variable):

# 1. Python makes educated guesses on whether variables are local or global. It assumes that any variable assigned a value in a function is local.
#    如果只是使用变量，变量在全局域中有定义，局部域中没有定义，则使用全局变量。
#    全局变量和局部变量同名，函数中默认使用局部变量。
num = 100   # 全局变量
def func():
	print(num)
	# num = num + 100   # local variable 'num' referenced before assignment, 如果不注释该行会报错，否则print(num) 会打印全局变量100
 
func()

# 2. 函数中如果要给全局变量赋值，使用关键字global

num = 100
def func():
	global num 
	num = num + 100 
	print(num)
func()
print(num)

 
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


# __getattr__:正常情况下，当我们调用类的方法或属性时，如果不存在就会报错AttributeError;
#             __getattr__()可以动态的返回一个属性，比如不存在score属性时，python解释器会试图调用__getattr__(self,'score')来获取属性，如果存在则不会调用__getattr__()
#             __setattr___(self, name, value): 类似__getattr__()，是尝试设置一个不存在属性时调用的函数
class Student(object):
	pass

s = Student()
# s.score  ==> 报错

class Student(object):
	def __init__(self, name):
		self._name = name

	def __getattr__(self, attr):
		if attr == 'score':
			return 90   
		if attr == 'age':
			return lambda : 25

s = Student('Lisa')
print(s._name)
print(s.score)
print(s.age())
print(s.gender)  # __getattr__()默认返回值是None

class Student(object):
	def __init__(self, name):
		self._name = name

	def __getattr__(self, attr):
		if attr == 'score':
			return 90   
		raise AttributeError('\'Student\' object has no attribute %s' % attr)

s = Student('Lisa')
print(s._name)
print(s.score)
# print(s.gender) # raise AttributeError


# 完全动态调用特性示例：REST API
class Chain(object):

	def __init__(self, path = ''):
		self._path = path

	def __getattr__(self, path):
		return Chain('%s/%s' % (self._path, path))

	def __str__(self):
		return self._path

print(Chain().status.user.timeline.list)  #/status/user/timeline/list

# __call__():直接对实例进行调用
class Student(object):
	def __init__(self, name):
		self._name = name
	def __call__(self):
		print('My name is : %s' % self._name)

s = Student('Michael')
print(s())

# 能被调用的对象就是一个Callable对象,callable()判断是否是Callable对象
print('test Callable object:')
print(callable(Student('')))
print(callable([1,2,3]))
print(callable(max))

# /users/:user/repos ==> REST API url 调用时:user用实际用户名替换

class Chain(object):
	def __init__(self, path = ''):
		self._path = path
	def __getattr__(self, path):
		return Chain('%s/%s' % (self._path, path))
	def __call__(self, path):
		return Chain('%s/%s' % (self._path, path))
	def __str__(self):
		return self._path

print(Chain().users('michael').repos)


# 枚举：Enum
from enum import Enum

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

print(Month.Jan)
print(Month.Jan.value)  # 1,自动赋值给成员的int常量，默认从1开始计数

for name,member in Month.__members__.items():
	print(name, '==>', member, ',', member.value)


# 更精确地控制枚举类型
from enum import Enum, unique

@unique   # @unique装饰器帮助检查保证没有重复值
class Weekday(Enum):
	Sun = 0
	Mon = 1
	Tue = 2
	Wed = 3 
	Thu = 4 
	Fri = 5 
	Sat = 6

print(Weekday.Mon)
print(Weekday['Mon'])
print(Weekday.Mon.value)
print(Weekday(1))
# print(Weekday[1])  # Error
# print(Weekday(7))  # ValueError

for name,member in Weekday.__members__.items():
	print(name, '==>', member, ',', member.value)

# type() 查看一个类型或变量的类型，也可以创建新的类型(正常情况下使用class定义时，python解释器也是通过调用type()函数创建class)

fn = lambda slef,name = 'World' : print('Hello %s ' % name)

H = type('Hello', (object,), dict(hello = fn)) # 创建Hello class，而不需要class定义
# type新建类型传入的3个参数：
#		1.class的名称
#  		2.继承的父类集合，Python支出多继承，如果只有一个父类，别忘了tuple的单元素写法
#		3.class的方法名称与函数绑定，这里把函数fn绑定到方法名hello上

h = H()
print(H.__name__)
print(type(H))
print(type(h))
h.hello('Michael')


# metaclass :元类，控制类的创建行为；根据metaclass创建类，先定义metaclass，然后创建类
#       实例创建过程：定义metaclass --> 创建类 --> 创建实例

class ListMetaclass(type): # metaclass是类的模板，必须从 type 类型派生
	def __new__(cls, name, bases, attrs):  # 参数： 1.cls:当前准备创建的类的对象; 2.创建类的名字； 3.创建类继承的父类集合； 4.创建类的方法和属性集合(dict)
		attrs['add'] = lambda self, value : self.append(value)
		return type.__new__(cls, name, bases, attrs)

class MyList(list, metaclass = ListMetaclass): # 定义类时，指定使用的metaclass,Python解释器在创建MyList时，通过ListMetaclass.__new__()来创建,因此，可以修改类的定义
	pass

L = MyList()
print(L)
L.add(1)
print(L)


# metaclass示例： ORM (Object Relational Mapping)
class Field(object):
	def __init__(self, name, column_type):
		self.name = name
		self.column_type = column_type
	def __str__(self):
		return '<%s,%s>' % (self.name, self.column_type)

class StringField(Field):
	def __init__(self, name):
		super(StringField, self).__init__(name, 'varchar(100)')

class IntegerField(Field):
	def __init__(self, name):
		super(IntegerField, self).__init__(name, 'bigint')

class ModelMetaclass(type):
	def __new__(cls, name, bases, attrs):
		if name == 'Model':
			return type.__new__(cls, name, bases, attrs)
		print('Found Model: %s' % name)
		mappings = dict()
		for k,v in attrs.items():
			if isinstance(v, Field):
				print('Found mapping: %s ==> %s' % (k,v) )
				mappings[k] = v
		for k in mappings.keys():
			attrs.pop(k)                  # 删除类属性
		attrs['__mappings__'] = mappings  # 属性名和列的映射
		attrs['__table___'] = name        # 假设表名和类名一致
		return type.__new__(cls, name, bases, attrs)

class Model(dict, metaclass = ModelMetaclass):

	def __init__(self, **kw):
		super(Model,self).__init__(**kw)

	def __getattr__(self, key):
		try:
			return self[key]
		except KeyError:
			raise AttributeError(r"'Model' object has no attribute '%s'" % key)

	def __setattr__(self, key, value):
		self[key] = value

	def save(self):
		fields = []
		params = []
		args = []

		for k, v in self.__mappings__.items():
			fields.append(v.name)
			params.append('?')
			args.append(getattr(self, k ,None))
		sql = 'insert into %s (%s) value (%s)' % (self.__table___,','.join(fields), ','.join(params))
		print('SQL: %s' % sql)
		print('ARGS: %s' % str(args))


#调用Orm
class User(Model):
	id = IntegerField('id')
	name = StringField('name')
	email = StringField('email')
	password = StringField('password')

u = User(id = 123, name = 'Lisa', email = 'test@git', password = 'pwd')
u.save()


## 八、 错误、调试和测试

# 所有错误类型都继承自 BaseException
#       常见的错误类型和继承关系： https://docs.python.org/3/library/exceptions.html#exception-hierarchy

# try...except...finally...类似java中的try...catch...finally；python中如果没有错误发生，可以在except语句块后面加一个else，当没有错误发生时，会自动执行else语句
try:
	print('try ...')
	r = 10/ int('2')
	print('resutl: ', r)
except ValueError as e:
	print('except: ', e)
except ZeroDivisionError as e:
	print('except: ', e)
else:
	print('no error.')
finally:
	print('finally...')
print('End')


# try...except 可以跨越层级调用，比如函数main()调用foo()，foo()调用bar()，结果bar()出错了，这时，只要main()捕获到了，就可以处理
# 调用栈：如果错误没有被捕获，就会一直往上抛，最后被Python解释器捕获，打印错误信息，然后程序退出

# logging模块：记录错误信息
import logging

def foo(s):
	return 10 / int(s)
def bar(s):
	return foo(s) * 2

def main():
	try:
		bar('0')
	except Exception as e:
		pass
#		logging.exception(e)  # 打印异常信息，程序继续执行

main()
print('End')

# 抛出异常 raise
def foo(s):
	n = int(s)
	if n == 0:
		raise ValueError('invalid value %s' % s)
	return 10 / n 

def bar():
	try:
		foo('0')
	except ValueError as e:
		print('ValueError')
		raise  # raise语句不带参数，表示把当前错误原样抛出

# 调试：
# 1. print() 打印
# 2. assert断言： assert n != 0, 'n is zero' ;上述断言表示，n!=0 应该是True, 断言失败会抛出AssertionError: n is zero; 启动时可以通过-O 关闭断言，当做pass来看 :python -O first.py
# 3. logging：输出文本  
#    import logging
#    logging.basicConfig(level = logging.INFO) # 设置日志的输出等级, 表示logging.info('error')也会输出到文本，级别从低到高依次：debug,info,warning,error
# 4. pdb调试器，命令行启动 python -m pdb first.py; Sublime Text3 的SublimeREPL插件可以启用pdb调试：b row ==> 在row行添加断点; r ==> 运行到断点处
# 5. IDE:vs code, pycharm等

# 单元测试：unittest模块
class Student(object):
	def __init__(self, name, score):
		self._name = name

		if not isinstance(score, int):
			raise ValueError('not a int value')
		self._score = score

import unittest

class TestDict(unittest.TestCase): # 编写单元测试，需要编写一个测试类，继承自unittest.TestCase
	def setUp(self):  # 每次调用一个test方法前执行
		print('setUp ...')

	def tearDown(self): # 每次调用一个test方法后执行
		print('tearDown ...') 


	def test_init(self):  # 测试方法需要以test开头，不以test开头的不被认为是测试方法，测试的时候不会执行
		s = Student('Lisa', 90)
		self.assertEqual(s._score, 90) # 判断相等
		self.assertTrue(isinstance(s, Student))  

		with self.assertRaises(ValueError):  # 期待抛出异常
			s = Student('Michael', '1')

	def test_fn(self):
		pass

# 运行单元测试： 
#    方式一：推荐，命令行输入 python -m unittest first  ==> first是测试类所在文件名
#    方式二：单元测试类所在文件添加如下代码
#if __name__ == '__main__':
#	unittest.main()

# 文档测试：
class Dict(dict):
    '''
    Simple dict but also support access as x.y style.

    >>> d1 = Dict()
    >>> d1['x'] = 100
    >>> d1.x
    100
    >>> d1.y = 200
    >>> d1['y']
    200
    >>> d2 = Dict(a=1, b=2, c='3')
    >>> d2.c
    '3'
    >>> d2['empty']
    Traceback (most recent call last):
        ...
    KeyError: 'empty'
    >>> d2.empty
    Traceback (most recent call last):
        ...
    AttributeError: 'Dict' object has no attribute 'empty'
    '''
    def __init__(self, **kw):
        super(Dict, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

if __name__=='__main__':
    import doctest    # python内置的文档注释模块，严格按照命令行的输入输出来判断测试结果是否正确，如果没有输出表示运行正确，否则会输出错误信息
    doctest.testmod()


## 九、同步IO编程    
#    Stream(流)：单向
#    同步IO, 异步IO(回调模式，轮询模式)

# 在磁盘上读写文件的功能都是由操作系统提供的，现代操作系统不允许普通的程序直接操作磁盘，所以读写文件就是请求操作系统打开一个文件对象(文件描述符)，然后通过操作系统提供的接口从这个文件对象中
#   读取数据，或把数据写入这个文件对象

# 读文件

try:
	f = open(r'E:\python\test.txt','r')  # 如果文件不存在，抛出IOError
	print(f.read()) # 一次读取文件的全部内容，python把内容读到内存，用一个str对象表示
finally:
	if f:
		f.close() # 关闭文件

#上述代码可以简化,使用with语句自动调用close()
with open(r'E:\python\test.txt','r') as f:
	print(f.read())

# read(size):每次最多读取size个字节内容
# readline()：每次读取一行内容
# readlines()：一次读取所有内容并按行返回list
with open(r'E:\python\test.txt','r') as f:
	for line in f.readlines():
		print(line.strip()) 

# file-like Object: 有read()方法的对象

# 二进制文件
#with open(r'E:\python\test.ico','rb') as f:
#	print(f.read())  # 输出16进制表示的字节

# 其他参数：
# f = open(r'E:\python\test.txt', 'r', encoding = 'gbk', errors='ignore) ; encoding指定读取文件的字符编码； 文本文件可能夹杂一些非法编码字符，UnicodeDecodeError, errors='ignore' 表示遇到错误编码时直接忽略

# 写文件：也是使用open(), 'w'表示写文本文件(如果文件已存在，直接覆盖，相当于删除后新写入一个文件),'wb'表示写二进制文件，'a'表示追加内容到文件末尾
with open(r'E:\python\testwrite.txt','w', encoding = 'gbk') as f:
	f.write('test 写入')


# 参照https://docs.python.org/3/library/functions.html#open
#Character	Meaning
#'r'		open for reading (default)
#'w'		open for writing, truncating the file first
#'x'		open for exclusive creation, failing if the file already exists
#'a'		open for writing, appending to the end of the file if it exists
#'b'		binary mode
#'t'		text mode (default)
#'+'		open a disk file for updating (reading and writing)
#'U'		universal newlines mode (deprecated)

# StringIO (内存中读写str,只能操作str)、BytesIO (内存读写bytes):使得内存中str、bytes的操作和读写文件有一致的接口 

print('test StringIO:')

from io import StringIO
f = StringIO()
print(f.write('hello'))
print(f.write(' '))
print(f.write('world !'))
print(f.getvalue())
print(f.tell())  # 获取stream position,可以通过f.seek(offset, whence = 0)调整position: offset表示偏移量(如果文件没有以'b'打开，无法使用负值)，whence 默认值0表示文件开头，1表示当前位置，2表示文件末尾


f = StringIO('Hello!\nHi!\nGoodbye!')
while True:
	s = f.readline()
	if s == '':
		break
	print(s.strip())


print('test BytesIO:')
from io import BytesIO
f = BytesIO()
print(f.write('中文'.encode('utf-8')))
print(f.getvalue())

f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f.read())


# 操作文件和目录：os模块可以直接调用操作系统提供的接口函数
import os
print(os.name)  # nt 是Windows系统; posix 是Linux、Unix或Mac OS X
# print(os.uname()) # 获取详细的系统信息，windows上不支持
# print(os.environ) # 系统的环境变量
print(os.environ.get('Maven')) # 获取指定环境变量的值
print(os.environ.get('Maven','default'))


# 操作文件好目录的函数一部分放在os模块中，一部分放在os.path模块中
print(os.path.abspath('.')) # 查看当前目录的绝对路径
print(os.path.join(r'E:\python','testDir')) # 显示某个目录下的指定目录的完整路径,这种拼接方式可以正确处理不同操作系统的路径分割符
os.mkdir(r'E:\python\testDir')  # 创建一个新目录，如果存在报错FileExistsError
os.rmdir(r'E:\python\testDir') # 删除一个目录
print(os.path.split(r'E:\python\test.txt'))  # 把路径拆分成两部分，后一个部分总是最后级别的目录或文件名，可以正确处理不同操作系统的路径分割符
print(os.path.splitext(r'E:\python\test.txt')) # 获取文件的扩展名
# 以上合并、拆分操作并不需要目录和文件真实存在，只是对字符串进行操作
os.rename(r'E:\python\testwrite.txt',r'E:\python\testwrite.py')  # 文件重命名，如果没有完整路径，表示当前文件夹下，文件不存在时FileNotFoundError
os.remove(r'E:\python\testwrite.py') # 删除文件

# 复制文件的函数在os模块中不存在！原因是复制文件并非操作系统提供的系统调用。可以使用IO,或者shutil模块
import shutil
shutil.copyfile(r'E:\python\test.txt', r'E:\python\test_copy.txt')
os.remove(r'E:\python\test_copy.txt')

print([x for x in os.listdir('.') if os.path.isdir(x)]) # 列出当前目录下的所有目录, 注意：os.path.isdir()的参数应该是路径，而os.listdir('.')得到的结果是名称集合,此处可以这么写因为是判断当前文件夹下
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']) # 列出当前目录下的py文件
print([x for x in os.listdir('.')])  # 列出当前目录下的所有文件和目录，不显示次级目录内容
print([x for x in os.listdir('./image')]) # 列出当前目录下的image目录下的文件和目录名
print('------')
print('ab' in 'abc') # 判断字符串包含另一个字符串, 返回True,False
print('abc'.find('ab')) # 判断字符串包含另一个字符串, 返回index,如果不包含则返回-1
print('abc'.find('ac'))


# 输出文件名包含s的所有文件的相对路径
def dirfile(s, path = '.',):
	global R
	files = [os.path.join(path, x) for x in os.listdir(path) if not os.path.isdir(os.path.join(path, x)) and (s.lower() in os.path.splitext(x.lower())[0]) ]
	dirs = [x for x in os.listdir(path) if os.path.isdir(os.path.join(path, x))]

	R = R + files

	for d in dirs:
		dirfile(s, os.path.join(path, d))


#R = []
#dirfile('a')
#print(R)

# 序列化,python中叫pickling,java中叫serialization
# 反序列化, unpickling
import pickle  # 实现序列化的模块
# python的pickle模块序列化和反序列化只能用于python，并且可能不同版本的python彼此都不兼容，因此，只能用pickle保存不重要的数据，不能成功反序列化也没有关系
d = dict(name='Bob', age=20, score=88)
print(pickle.dumps(d))  #dumps()把任意对象序列化成一个bytes,然后就可以手动把这个bytes写入文件

with open(r'E:\python\pickle.txt','wb') as f:
	pickle.dump(d, f)   #dump() 直接把对象序列化后写入一个file-like object

# 反序列化方式： 1.把内容读到一个bytes,然后用pickle.loads()方式反序列化出对象
#				2.直接用pickle.load()方法从一个file-like object 中反序列化出对象
with open(r'E:\python\pickle.txt','rb') as f:
	di = pickle.load(f)
print(di)

# JSON：在不同的编程语言之间传递对象，是一种序列化的标准格式，JSON和Python数据类型对应如下：
# JSON类型	    Python类型
#  {}	          dict
#  []	          list
# "string"	      str
# 1234.56	    int或float
# true/false	True/False
# null            None

import json # python内置的python对象和json格式转换的模块

d = dict(name='Bob', age=20, score=88)
print(json.dumps(d)) # dumps()方法返回一个str,表示标准的JSON (JSON标准规定JSON编码时UTF-8); dump()方法可以直接把json写入一个file-like object

with open(r'E:\python\json.txt','w') as f:
	json.dump(d, f)

json_str = '{"name": "Bob", "age": 20, "score": 88}'
d = json.loads(json_str) # loads()方法把json字符串反序列化成对象；load()方法从file-like object 中读取字符串并反序列化
print(d)


# 序列化类实例：
import json

class Student(object):
	def __init__(self, name, age, score):
		self.name = name
		self.age = age
		self.score = score

s = Student('Bob', 20, 90)
#print(json.dumps(s))  # 直接序列化抛出TypeError

# https://docs.python.org/3/library/json.html#json.dumps 参看文档

def student2dict(std):
	return {
		'name': std.name,
		'age' : std.age,
		'score': std.score
	}

print(json.dumps(s, default = student2dict)) # student实例首先被student2dict()函数转换成dict,然后再序列化成JSON

print(s.__dict__) # 实例的__dict__属性

def dict2student(d):
	return Student(d['name'], d['age'], d['score'])

print(json.loads('{"name": "Bob", "age": 20, "score": 88}', object_hook = dict2student)) # 同理，反序列化先将str转换成dict，再通过 object_hook的函数将dict转换成Student对象

obj = dict(name='小小', age = 22)
print(json.dumps(obj, ensure_ascii = True)) # ensure_ascii默认是True
print(json.dumps(obj, ensure_ascii = False))


## 十、进程(Process)和线程(Thread)
# 多任务处理： 1.多进程； 2. 单进程多线程； 3. 多进程多线程

# Unix/Linux 操作系统提供一个fork()系统调用，普通函数调用，调用一次，返回一次，fork()调用一次，返回两次，因为操作系统自动把当前进程(父进程)复制了一份(子进程)，然后分别在父进程和子进程内返回。
#            子进程永远返回0，父进程返回子进程的ID。一个父进程可以fork出很多子进程，所以父进程要记下每个子进程的ID，而子进程只需要调用getppid()就可以拿到父进程的ID。

#import os 
#print('Process (%s) start...' % os.getpid())

#pid = os.fork()  # only work on Linux/Unix/Mac， 通过fork调用，一个进程在接到新任务时就可以复制出一个子进程来处理新任务
#if pid == 0 : 
#	print('i am child process (%s) and my parent process is (%s)' % (os.getpid(), os.getppid()))
#else : 
#	print('i (%s) just created a child process (%s)' % (os.getpid(), pid))


# multiprocessing模块：跨平台的多进程模块

# 在Unix/Linux下，multiprocessing模块封装了fork()调用，使我们不需要关注fork()的细节。
# 由于Windows没有fork调用，因此，multiprocessing需要“模拟”出fork的效果，父进程所有Python对象都必须通过pickle序列化再传到子进程去，
#    所以，如果multiprocessing在Windows下调用失败了，要先考虑是不是pickle失败了

from multiprocessing import Process
import os

def run_proc(name):
	print('Run child process %s (%s)...' % (name, os.getpid()))

#if __name__ == '__main__':   # Make a script both importable and executable, 直接执行时为True，import导入该文件时为False, 即导入时不会执行
                                                                                       #   上面所写的测试代码，import 导入时依然会执行
#	print('Parent process %s.' % os.getpid())
#	p = Process(target = run_proc, args = ('test',))
#	print('child process will start...')
#	p.start()   # 开始一个子进程，会将上面的测试代码重新又运行一遍
#	p.join()  # 等待p进程结束
#	print('child procss end.')


# Pool：进程池，可以批量创建子进程


# 以下代码应单独提出到一个独立的py文件中执行，当前py中有过多测试代码，每个新进程都会执行一遍
# from multiprocessing import Pool
# import os, time, random

# def long_time_task(name):
# 	print('Run task %s (%s)...' % (name, os.getpid()))
# 	start = time.time()
# 	time.sleep(random.random() * 3)
# 	end = time.time()
# 	print('Task %s runs %0.2f seconds.' % (name, (end - start)))

# if __name__ == '__main__':
# 	print('Parent process %s.' % os.getpid())
# 	p = Pool(4)  # Pool 默认大小是CPU核心数
# 	for i in range(5):
# 		p.apply_async(long_time_task, args=(i,))
# 	print('Waiting for all subprocesses done...')
# 	p.close()   # join()方法等待所有子进程执行完毕，join()调用之前需先调用close()，调用close()之后就不能继续添加新的Process
# 	p.join()
# 	print('All subprocesses done.')

# 执行结果(命令行运行)： Pool池只有4，所以同时只能运行4个进程；
#          但是在Sublime Text中执行时，进程按照顺序执行，一个进程执行完再执行下一个进程 (不清楚原因)
# Parent process 21168.
# Waiting for all subprocesses done...
# Run task 0 (4748)...
# Run task 1 (22740)...
# Run task 2 (23780)...
# Run task 3 (16532)...
# Task 3 runs 0.92 seconds.
# Run task 4 (16532)...
# Task 2 runs 1.92 seconds.
# Task 1 runs 1.98 seconds.
# Task 0 runs 2.99 seconds.
# Task 4 runs 2.92 seconds.
# All subprocesses done.


# 子进程: subprocess模块：启动一个子进程，然后控制其输入输出
#       关于子进程更多内容参考文档
import subprocess

print('$ nslookup www.python.org')
r = subprocess.call(['nslookup','www.python.org']) # python代码中运行命令 nslookup www.python.org ;该命令用于查询DNS记录，查看域名解析是否正常，命令行中可直接运行
print('Exit Code:', r) 
print('-------')

# 相当于在命令行输入：
#   nsloookup
#   set q=mx
#   python.org
#   exit
import subprocess
print('$ nslookup')
p = subprocess.Popen(['nslookup'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
output,err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('gbk'))
print('Exit Code:', p.returncode)


# 进程间通信：multiprocessing模块中Queue、Pipes等，代码示例如下：

# from multiprocessing import Process, Queue
# import os, time, random

# 写数据进程执行的代码:
# def write(q):
#     print('Process to write: %s' % os.getpid())
#     for value in ['A', 'B', 'C']:
#         print('Put %s to queue...' % value)
#         q.put(value)
#         time.sleep(random.random())

# # 读数据进程执行的代码:
# def read(q):
#     print('Process to read: %s' % os.getpid())
#     while True:
#         value = q.get(True)
#         print('Get %s from queue.' % value)

# if __name__=='__main__':
#     # 父进程创建Queue，并传给各个子进程：
#     q = Queue()
#     pw = Process(target=write, args=(q,))
#     pr = Process(target=read, args=(q,))
#     # 启动子进程pw，写入:
#     pw.start()
#     # 启动子进程pr，读取:
#     pr.start()
#     # 等待pw结束:
#     pw.join()
#     # pr进程里是死循环，无法等待其结束，只能强行终止:
#     pr.terminate()



#  多线程：Python的线程是真正的Posix Thread，而不是模拟出来的线程。
#         Pythont标准库提供了两个模块: _thread和threading, _thread是低级模块，threading是高级模块，对_thread进行了封装。

import time,threading

def loop():
	print('thread %s is running...' % threading.current_thread().name) # current_thread()返回当前线程的实例，主线程实例的名字叫MainThread,子线程默认名为Thread-1,Thread-2,...
	n = 0

	while n < 5:
		n = n + 1
		print('thread %s >>> %s' % (threading.current_thread().name, n))
		time.sleep(1)
	print('thread %s end' % threading.current_thread().name)

print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('thread %s end' % threading.current_thread().name)

# Lock: 确保某段关键代码只能由一个线程从头到尾完整执行(存在死锁)
#  多进程中同一个变量各自有一份拷贝存在于每个进程中，互不影响，而多线程中，所有变量都由所有线程共享。所以，任何一个变量都可以被任何一个线程修改。

import time,threading

balance = 0
lock = threading.Lock() # 创建锁

def change_it(n):
	global balance
	balance = balance + n 
	balance = balance - n 

def run_thread(n):
	for i in range(100000):
		lock.acquire() # 获取锁
		try:
			change_it(n)
		finally:
			lock.release() # 释放锁

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance) 


# Python解释器由于设计时有GIL全局锁，导致了多线程无法利用多核。多线程的并发在Python中就是一个美丽的梦。

# ThreadLocal:
class Student(object):
	def __init__(self, name):
		self.name = name

import threading 

local_school = threading.local() # 创建ThreadLocal对象

def process_student():
	std = local_school.student 
	print('hello, %s (in %s)' % (std, threading.current_thread().name))

def process_thread(name):
	local_school.student = name  # 绑定ThreadLocal的student
	process_student() 

t1 = threading.Thread(target=process_thread,args=('Alice',),name='Thread-A')
t2 = threading.Thread(target=process_thread,args=('Bob',),name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()

# 计算密集型 vs IO密集型
#  python脚本语言运行效率低，不适合计算密集型任务

# 分布式进程：multiprocessing的子模块manager支持把多进程分布到多台机器上

# # task_master.py

# # windows 查看端口占用进程： 
# # netstat -ano
# # netstat -ano|findstr "PID number"
# # tasklist|findstr "PID number"

# import random,time,queue
# from multiprocessing.managers import BaseManager

# task_queue = queue.Queue()  # 发送任务的队列
# result_queue = queue.Queue() # 接收结果的队列

# class QueueManager(BaseManager): # 继承BaseManager
# 	pass

# def return_task_queue():
# 	return task_queue

# def return_result_queue():
# 	return result_queue


# if __name__ == '__main__':
# 	# 把两个队列注册到网络上
# #	QueueManager.register('get_task_queue', callable=lambda : task_queue)  # pickle序列化不支持匿名函数
# #	QueueManager.register('get_result_queue', callable=lambda : result_queue)
# 	QueueManager.register('get_task_queue', callable=return_task_queue)  # pickle序列化不支持匿名函数
# 	QueueManager.register('get_result_queue', callable=return_result_queue)


# 	manager = QueueManager(address=('127.0.0.1',5000),authkey=b'abc') # 绑定端口5000,设置验证码abc

# 	manager.start() # 启动Queue

# 	#通过网络访问的Queue对象
# 	task = manager.get_task_queue()  
# 	result = manager.get_result_queue()

# 	# 添加几个任务
# 	for i in range(10):
# 		n = random.randint(0, 10000)
# 		print('put task %d...' % n)
# 		task.put(n)

# 	# 从result队列读取结果
# 	print('Try get Results...')
# 	for i in range(10):
# 		r = result.get()
# 		#r = result.get(timeout=10)
# 		print('result: %s' % r)

# 	# 关闭
# 	manager.shutdown()
# 	print('master exit')


# # task_worker.py

# import time,sys,queue
# from multiprocessing.managers import BaseManager

# class QueueManager(BaseManager):
# 	pass

# # 由于这个QueueManager只从网络上获取Queue，所以注册时只提供名字:
# QueueManager.register('get_task_queue')
# QueueManager.register('get_result_queue')

# # 连接到运行task_master.py的机器
# server_addr = '127.0.0.1'
# print('Connect to server %s ' % server_addr)

# m = QueueManager(address=(server_addr,5000),authkey=b'abc')

# m.connect()

# # 获取Queue对象
# task = m.get_task_queue()
# result = m.get_result_queue()

# # 获取任务，并把结果放入result
# for i in range(10):
# 	try:
# 		n = task.get(timeout=1)
# 		print('run task %d * %d' % (n,n))
# 		r = '%d * %d = %d' % (n,n,n*n)
# 		time.sleep(1)
# 		result.put(r)
# 	except Queue.Empty:
# 		print('task queue is empyt')

# # 结束
# print('worker exit')


## 十一、正则表达式： 默认是贪婪匹配

# re模块
import re

print(re.match(r'^\d{3}\-\d{3,8}$','010-12345')) # match匹配成功返回一个Match对象，否则返回None
print(re.match(r'^\d{3}\-\d{3,8}$','0101-12345'))

# 上述匹配过程： 1. 编译正则表达式； 2.用编译后的正则表达式去匹配字符串

# 对于需要多次重复使用的正则表达式，可以使用预编译：
re_telephone = re.compile(r'^\d{3}\-\d{3,8}$')
print(re_telephone.match('010-12345'))


# 切分字符串
print(re.split(r'\s+','a b   c')) 
print(re.split(r'[\s,;]+','a,b;; c   d'))

# 分组
m = re.match(r'^(\d{3})\-(\d{3,8})$','010-12345')
print(m.group(0)) # group(0)是原始字符串
print(m.group(1))
print(m.group(2))
print(m.groups()) # 获取除了原始字符串的所有分组子串


regular = r'((\w+[\.]\w+)|(\w+))@\w+[\.]?\w+'
email1 = r'someone@gmail.com'
email2 = r'bill.gates@microsoft.com'
email3 = r'b@microsoft.com'
email4 = r'a.a@microsoft.com'
print(re.match(regular,email1))
print(re.match(regular,email2))
print(re.match(regular,email3))
print(re.match(regular,email4).groups())


regular = r'((<([\w\s]+)>\s+\w+)|(\w+))@\w+[\.]\w+'
email1 = r'<Tom Paris> tom@voyager.org'
email2 = r'bob@example.com'

m = re.match(regular, email1)
print(m)
print(m.group(3))
m = re.match(regular, email2)
print(m)
print(m.group(1))



## 十二、常用内建模块

# datetime: 处理日期和时间, https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
from datetime import datetime # datetime模块中还包含一个datetime类，需要导入datetime类
now = datetime.now() # 获取当前datetime
print(now)
print(type(now))

dt = datetime(2018,10,20,12,59)
print(dt)

print(dt.timestamp()) # 将datetime转换成timestamp(1970-1-1 00:00:00 UTC+0:00为0)，返回浮点数，小数位表示毫秒数

print(datetime.fromtimestamp(1429417200.0)) # timestamp转换成datetime,转换的datetime是当前操作系统设置的时区
print(datetime.utcfromtimestamp(1429417200.0)) # datetime是UTC标准时区的时间

print(datetime.strptime('2018-10-20 17:59:59','%Y-%m-%d %H:%M:%S')) # str转datetime：结果没有时区信息
print(datetime.now().strftime('%a, %b %d %H:%M')) # datetime转str


from datetime import datetime,timedelta
now = datetime.now()
print(now)
print(now + timedelta(hours=10))
print(now - timedelta(days=1))
print(now + timedelta(days=2,hours=12))


from datetime import datetime,timedelta,timezone

tz_utc_8 = timezone(timedelta(hours=8)) #创建时区UTC+8：00
now = datetime.now()
dt = now.replace(tzinfo=tz_utc_8) # tzinfo是datetime的时区属性，默认是None，replace强制设置为UTC+8:00
dt = now.replace(tzinfo=timezone(timedelta(hours=1)))
print(dt)

utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc) #获取utc时间(带时区的datetime)并强制设置时区为UTC+0:00
print(utc_dt)
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8))) #将时区转换成UTC+8:00(北京时间)
print(bj_dt)
tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9))) # 东京时间(UTC+9:00)
print(tokyo_dt)
tokyo_dt = bj_dt.astimezone(timezone(timedelta(hours=9))) # 东京时间(UTC+9:00)
print(tokyo_dt)


# 2015-1-21 9:01:30 UTC+5:00 转换为timestamp
from datetime import datetime,timezone,timedelta

print(os.path.dirname(os.__file__)) # 获取py文件模块路径

def to_timestamp(dt_str, tz_str):
	time = datetime.strptime(dt_str,'%Y-%m-%d %H:%M:%S')

	hour = int(tz_str[3:-3])
	utc_time = time.replace(tzinfo=timezone(timedelta(hours=hour)))

	return utc_time.timestamp()

print(to_timestamp('2015-6-1 08:10:30', 'UTC+7:00'))
print(to_timestamp('2015-5-31 16:10:30', 'UTC-09:00'))



# collections:集合模块 

# namedtuple
from collections import namedtuple
Point = namedtuple('Point',['x','y']) # 自定义tuple对象，规定tuple元素的个数
p = Point(1,2)
print(p.x,p.y)
print('p is an instance of Point:',isinstance(p, Point))
print('p is an instance of tuple:',isinstance(p, tuple))

Circle = namedtuple('Circle',['x','y','r'])

# deque : 双向列表，适用于栈、队列,插入删除效率比list高
from collections import deque
q = deque(['a','b','c'])
q.append('x')
q.appendleft('y')
print(q)
print(q.pop())
print(q.popleft())


# defaultdict: dict当key不存在时抛出KeyError,defaultdic当key不存在时返回一个默认值
from collections import defaultdict
dd = defaultdict(lambda : 'N/A')  # 默认值通过函数调用返回

dd['key1'] = 'abc'
print(dd['key1'])  # 返回'abc'
print(dd['key2'])  # 返回'N/A'


# OrderedDict : 使key有序,按照插入顺序排列
from collections import OrderedDict
od = OrderedDict([('a',1),('b',2),('c',3)])
print(od)


# 使用OrderedDict实现一个FIFO的dict
from collections import OrderedDict

class LastUpdatedOrderDict(OrderedDict):
	def __init__(self, capacity):
		super(LastUpdatedOrderDict, self).__init__()
		self._capacity = capacity

	def __setitem__(self, key, value):
		containsKey = 1 if key in self else 0 

		if len(self) - containsKey >= self._capacity:
			last = self.popitem(last=False)
			print('Remove:',last)
		if containsKey:
			del self[key]
			print('set:',(key,value))
		else: 
			print('add:',(key,value))

		OrderedDict.__setitem__(self,key,value)

fifo = LastUpdatedOrderDict(3)
fifo['x'] = 1 
fifo['y'] = 2
fifo['z'] = 3 
fifo['m'] = 4
print(fifo)


# ChainMap: 把一组dict串起来并组成一个逻辑上的dict，ChainMap本身也是一个dict，但是查找的时候会按照顺序在内部的dict依次查找

# from collections import ChainMap
# import os, argparse

# # 构造缺省参数:
# defaults = {
#     'color': 'red',
#     'user': 'guest'
# }

# # 构造命令行参数:
# parser = argparse.ArgumentParser()
# parser.add_argument('-u', '--user')
# parser.add_argument('-c', '--color')
# namespace = parser.parse_args()
# command_line_args = { k: v for k, v in vars(namespace).items() if v }

# # 组合成ChainMap:
# combined = ChainMap(command_line_args, os.environ, defaults)

# # 打印参数:
# print('color=%s' % combined['color'])
# print('user=%s' % combined['user'])



# Counter:计数器，dict子类
from collections import Counter

c = Counter()

for ch in 'Programming':
	c[ch] = c[ch] + 1
print(c)



# Base64:用64位字符来表示任意二进制数据, Base编码把3字节二进制数据编码为4字节文本数据，不是3的倍数时，末尾用\x00字节补足，编码末尾加上1或2个'=',表示补了多少字节;Base64是一种查表编码方法，不能用于加密，适用于小段内容的编码，
#如数字证书签名、cookie内容，标准Base64编码可能会有'=',在url或cookie会有歧义，很多Base64会把'=' 去掉

import base64

print(base64.b64encode(b'binary\x00string'))
print(base64.b64decode(b'YmluYXJ5AHN0cmluZw=='))
print(base64.b64encode(b'i\xb7\x1d\xfb\xef\xff'))
print(base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff')) # "url safe"的base64编码，实际上是将'+','/'分别替换为'-','_'
print(base64.urlsafe_b64decode('abcd--__'))


# 自定义能处理去掉'='的base解码函数
def safe_base64_decode(s):
	m = 4 - len(s) % 4 
	while 0 < m < 4 :
		s = s + b'='
		m = m - 1 
	return base64.b64decode(s) 


# 测试:
assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print('ok')


# struct: bytes和其他二进制数据类型转换，https://docs.python.org/3/library/struct.html#format-characters

# Python不适合编写底层操作字节流的代码，对性能要求不高的地方可以使用struct模块
import struct 
print(struct.pack('>I',10240099))  # pack把任意数据类型变成bytes：1.第一个参数是处理指令，'>I':'>'表示字节顺序是big-endian,'<'表示little-endian,也就是网络序，'I'表示4字节无符号整数

print(struct.unpack('>IH',b'\xf0\xf0\xf0\xf0\x80\x80')) # unpack把bytes变成相应的数据类型：'I'：4字节无符号整数；'H':两字节无符号整数

# 位图分析示例：
s = b'\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\x80\x02\x00\x00\x68\x01\x00\x00\x01\x00\x18\x00' # 位图前30个字节
# BMP格式采用小端方式存储数据，文件头的结构按顺序如下：

# 两个字节：'BM'表示Windows位图，'BA'表示OS/2位图；
# 一个4字节整数：表示位图大小；
# 一个4字节整数：保留位，始终为0；
# 一个4字节整数：实际图像的偏移量；
# 一个4字节整数：Header的字节数；
# 一个4字节整数：图像宽度；
# 一个4字节整数：图像高度；
# 一个2字节整数：始终为1；
# 一个2字节整数：颜色数。
print(struct.unpack('<ccIIIIIIHH',s))


# 判断是否是.bmp文件
import struct
def bmp_info(data):
	s = struct.unpack('<ccIIIIIIHH', data[:30])

	if s[0] != b'B' and s[1] != 'M':
		return None

	return {'width': s[6], 'height': s[7],'color': s[9]}


# hashlib:提供常见的摘要算法(又称哈希算法、散列算法，把任意长度的数据转换成一个长度固定的数据串)，如MD5,SHA1
#         摘要函数是一个单向函数，计算摘要(digest)很容易，但是通过digest反推数据却十分困难。可以用于发现原始数据是否被篡改过。不同数据通过摘要算法也有可能得到相同的摘要(碰撞)，但是非常困难。
#         摘要算法不是加密算法（因为无法通过摘要反推明文），只能用于防篡改，但是它的单向计算特性决定了可以在不存储明文口令的情况下验证用户口令。(如在数据库中只保存用户密码的摘要，还可以通过加salt,处理简单密码)

import hashlib 

md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
md5.update('the amount of data is large enough, so use another update()'.encode('utf-8'))
print(md5.hexdigest()) # 返回128bit(32 bytes),如果数据有改动，将会返回完全不同的结果

import hashlib
sha1 = hashlib.sha1()
sha1.update('how to use md5 in python hashlib?'.encode('utf-8'))
sha1.update('the amount of data is large enough, so use another update()'.encode('utf-8'))
print(sha1.hexdigest()) # 返回160bit(40 bytes)


# hmac: Hmac(Keyed-Hash Message Authentication Code)算法(https://en.wikipedia.org/wiki/HMAC)
import hmac
message = b'Hello World!'  # 原始消息，bytes类型
key = b'secret'    # 随机key，类似于加salt，bytes类型
h = hmac.new(key, message, digestmod='MD5') # hash使用MD5算法
# 如果消息过长，可以多次调用h.update(msg)
print(h.hexdigest())  # 输出长度和使用的原始hash算法返回长度一致



# itertools: 操作迭代对象，返回的是Iterator
# import itertools
# natuals = itertools.count(1)  # count()创建一个无限自然数迭代器，只能按ctrl + c 停止,不能直接在sublime3 运行，会让sublime3 失去响应，应在命令行中运行
# for n in natuals:
# 	print(n)

# import itertools
# cs = itertools.cycle('abc') # cycle()把传入的序列无限重复下去，也是无限迭代器
# for c in cs:
# 	print(c) # 输出'a','b','c','a','b','c',......

import itertools
ns = itertools.repeat('AB',3) # repeat()重复一个元素，如果没有第二个参数限定重复次数，将会把元素无限重复下去
for n in ns:
	print(n)


import itertools
natuals = itertools.count(1)
ns = itertools.takewhile(lambda x: x <= 10, natuals) # takewhile()根据条件判断截取一个有限序列, 注意该方法是截取(根据判断条件，两刀割，截取前部分，如itertools.takewhile(lambda x : x > 10, natuals) 得到的是空)
print(list(ns))


for c in itertools.chain('ABC','XYZ'): # chain()串联迭代对象，形成一个更大的迭代器
	print(c)

for key,group in itertools.groupby('AAABBBCCAAA'): # 把迭代器中相邻的重复元素挑出来放在一起
	print(key,list(group))

for key,group in itertools.groupby('AaaBbCcaAa', lambda x : x.upper()): # groupby 可以传入函数，只要两个元素通过函数得到的返回值相等，就被认为是一组
	print(key,list(group))


# 计算圆周率
def pi(N):
    ' 计算pi的值 '
    # step 1: 创建一个奇数序列: 1, 3, 5, 7, 9, ...
    ns = itertools.count(start = 1, step = 2)
    # step 2: 取该序列的前N项: 1, 3, 5, 7, 9, ..., 2*N-1.
    ns = itertools.takewhile(lambda x : x < 2*N, ns)
    # step 3: 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...
    rc = itertools.cycle([4,-4])
    ns = map(lambda x : next(rc) / x ,ns)
    # step 4: 求和:
    return sum(ns)


# 测试:
print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))
assert 3.04 < pi(10) < 3.05
assert 3.13 < pi(100) < 3.14
assert 3.140 < pi(1000) < 3.141
assert 3.1414 < pi(10000) < 3.1415
print('ok')



# contextlib
def Query(object):

	def __init__(self, name):
		self.name = name
	
	def __enter__(self):
		print('Begin')
		return self

	def __exit__(self,):


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
