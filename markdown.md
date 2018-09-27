## 分级标题 (*\# 号后需要空格，否则无效*)
# 一级标题
## 二级标题
### 三级标题
###### 六级标题  
>区块引用
>> 嵌套引用
>>> 嵌套引用2

> 引用段落1 
   引用段落2
   引用段落3


----
分割线
<br />
*斜体* (\*后不跟空格)
<br />
**粗体**
<br />
[Markdown syntax](https://github.com/cdoco/markdown-syntax "Markdown syntax")

<https://www.baidu.com>

[百度链接][1]

[1]:https://www.baidu.com 


```java
  system.out.println("java code")
```

## 插入图片
- 方式1：
<br /> 
```
插入换行符\<br />
```
<br /> 
![vbs处理.PNG](https://upload-images.jianshu.io/upload_images/14080660-bde490ea14204563.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

-方式2：
<br />
![vbs处理.png][2]

[2]:https://upload-images.jianshu.io/upload_images/14080660-bde490ea14204563.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240

**使用方式2插入图片，在简书中需要换行，否则无显示**

[java 工匠](https://czwer.github.io/2016/11/16/Dubbo+Cat%E5%88%86%E5%B8%83%E5%BC%8F%E6%9C%8D%E5%8A%A1%E6%90%AD%E5%BB%BA/)


[分页查询](https://my.oschina.net/vbird/blog/1504259)
[MySql分页查询](https://segmentfault.com/a/1190000008859706)

- [分级标题](#分级标题) *页内锚点连接，需要对应标题*  
 **简书上无法使用这种锚点方式,github可以使用**

~~删除线~~

## 无序列表(*使用 \*, -, 或 + 表示无序列表*)
 * row1
 - row2
 + row3

## 有序列表
 1. row1
 2. row2
 3. row3

## 表格

1. 不管是哪种方式, 第一行为表头, 第二行分隔表头和主体部分, 第三行开始每一行为一个表格行。
2. 列于列之间用管道符`|`隔开。原生方式的表格每一行的两边也要有管道符。
3. 第二行还可以为不同的列指定对齐方向。默认为左对齐, 在`-`右边加上`:`就右对齐。

 | col1 | col2 | col3 | 
 | - | - | - | 
 | value1 | value2 | value3 | 

##LaTex公式(*github不支持* )
质能方程 $ E = m * c ^2 $
$$ s ^ 4 $$

## 代办事项(*简书中不支持*)
* [ ] 早起跑步
* [x] 看书

*[ ] 早起跑步
*[x] 看书
<br />

[ ] 早起跑步
[x] 看书