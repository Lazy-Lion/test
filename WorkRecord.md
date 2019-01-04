* [运维项目](#运维项目)
* [Elipse调试快捷键](#Elipse-调试快捷键)
* [代码管理](#代码管理)
* [通过url直接进入指定页面](#通过url直接进入指定页面)
* [前后端数据传输](#前后端数据传输)
* [权限管理](#权限管理)
* [DataBase](#DataBase)
* [第一屏](#第一屏)
    * [增加人员卡口设备类型](#增加人员卡口设备类型)
    * [上传图片改用海鸥接口](#上传图片改用海鸥接口)
    * [工单报修](#工单报修)
* [第二屏](#第二屏)
    * [视频设备管理，必填项加\*](#视频设备管理，必填项加\*)
    * [研判报告](#研判报告)
* [页面样式]

## 页面样式
style: "text-align: center; overflow: hidden; white-space: nowrap; text-overflow: ellipsis;"
使用以上样式时，需要显示的内容太多时，会用省略号代替，有时需要鼠标悬浮时显示完整内容，此时可以不用添加mouseover事件，而只需要对内容所在容器(如div，span)添加title，title为完整内容，鼠标悬停时自动显示title内容。

## 运维项目：
 一机一档页面： http://localhost:8090/maintenance/deviceArchive/deviceArchiveShow?auth_userCode=god
 
 http://172.16.233.73:8080/maintenance/deviceArchive/deviceArchiveShow?auth_userCode=god
 <br />
 使用的工具： idea + tomcat 7 + gradle构建(注： gradle 和 maven的区别)<br />
 代码配置文件:WEB-INF\application.properties
 
 gradle 安装(注意版本)<br />
 idea 导入gradle项目
 <br/>
 <br />
 页面展示：.ftl文件 -> 前后台数据交互：对应的js文件 -> js文件访问对应的api文件映射访问后台数据 -> 后台使用mybatis交互数据库(dao + mapper) 

具体项目：
用户名、密码： B_RS_RY
Device
UserMapper.xml
UserService.java
(摄像机ID号 -> sbbh; 设备名称 -> sbmc; 所属设备分组 -> fzbh; 摄像机类型 -> sxjlx; 摄像机厂商 -> csmc (Sxjcs); 辖区公安机关 -> yhz; 监控区域类型 -> jkqylx; 摄像机所属部门 -> sxjssbm; 摄像机位置类型 -> wzlx; 联网属性 -> lwsx; 生命周期 -> sbsmzt; 设备审核状态 -> sbshzt)

设备昵称(即设备别名)：
设备品牌：
用户名：
密码：

改动文件：deviceArchive.ftl,BSssbSbxxMapper.xml,deviceArchiveInit.js,DeviceArchiveApi.java,DeviceArchiveBaseMsgApi.java,DeviceVo.java,BSssbSbxxVo.java
1.增加设备昵称搜索：sbsc (sbbm)： 



## Elipse 调试快捷键
 F5: 单步调试，进入函数内部
 F6: 单步调试，不进入函数内部
 F7: 由函数内部返回到调用处
 F8: 执行到下一个断点

## 代码管理
  - 主线: default分支
  - 
## 前端silverlight 提供组件
C# 提供dll文件时，除了ZJGS.dll外其他都需要替换对应xap以及ZJCM.UI.xap两处，xaml改动也是在dll中
## 通过url直接进入指定页面
 例： http://localhost:8888/ezView/VideoShell.html?userName=admin&page=SPSBGL#ZJSB18  <br />
 表示进入第二屏的视频设备管理页面<br />
 页面信息获取 **B_QJ_CD** 表:<br />
 select * from B_QJ_CD where JDZWM = '视频设备管理'
 
## 调试第二屏时，直接使用url访问形式访问第二屏页面，否则无法进入断点 
http://localhost:8888/ezView/VideoShell.html?userName=admin

## 前后端数据传输
  实体类：DhInfo

## 权限管理
角色、用户

## DataBase
  194 EZVIEW B_QJ_XTPZ : 配置表
  B_QJ_CD : 页面头菜单栏目录数据表

## 第一屏
#### 增加人员卡口设备类型（第一屏幕左边栏主页显示）
(**问题：不同分支的前后端代码不一致，后端分支的一些改动没有体现在当前使用前端代码的分支上，导致出现一些意外的bug；该项目就是后端对设备数据的cache改动，导致前端获取的设备数据一直为空**)

前台代码 ： 
 ZJGS.UI ->  LeftMenu文件夹 -> GisLeftMenu.xaml.cs : LoadGroupTree()
 TIT.ZNH.ZJCM.UI.AuthCache : LoadAuthCache()
 
 194 **EZVIEW.B_QJ_XTPZ** 表, BLM = sbfzpz, pzz = 1,1;0,1;1,2;0,6|1
   需要修改 pzz -> 1,1;0,1;1,2;0,4;0,6|1 (根据实际情况修改，只需增加 0,4 即可)
   
后台代码： 
  com.tit.znh.zj.cm.common.ComCache ： SbxxCache m_sbxxCache，<br />
  com.tit.znh.zj.cm.common.SbxxCache
  com.tit.znh.zj.cm.service.ServiceZJCMCM : queryQxxx()
```java        
    initSbxx(connection);
		initSbkz(connection);
		initSpfz(connection);
		initKkfz(connection);
		
		//初始化缓存，分别查询设备信息和视频分组(或卡口分组)信息，然后通过设备号将两个map结果
		//关联，得到设备对应的分组
```
   
 B_SPJK_SPFZB   --> 视频分组类型和名称
 B_SPJK_SPFZMX   ---> 视频分组关系表
 B_SSSB_KKFZMX   ---> 卡口分组关系表
 
 B_SSSB_SBXX    ----->
 B_SSSB_SBDQZTXX   ---->    设备信息的3张表
 B_QJ_PY        ---->
 
 B_QJ_DMX ----> pzz中的数字代码表示的内容

#### 上传图片改用海鸥接口
  地图作战 -> 人员轨迹 -> 左边栏人脸照片上传 <br />
  前台代码： ZJGS.UI ->  Trace文件夹 ->  PersonTrace.xaml.cs ： Image_MouseLeftButtonUp() <br />
  修改上传使用接口，改用海鸥提供的接口<br />
  接口服务地址： http://10.84.100.231:8080/haioumate/api/upload/uploadMultipleFile <br />
  服务test地址： http://10.84.100.231:8080/haioumate/testUpload.html
  <br />
  服务地址存入194 **EZVIEW.B_QJ_XTPZ** 表， tpscfw
  
  
  silverLight中不能直接通过路径构造文件流，需要通过对话框获取(在传输文件流时遇到的问题)
  
  代码模拟http post请求上传图片,模拟上传二进制文件( **Fiddler** 抓取上传图片请求格式)：
    与post其他数据不同，模拟post multipart/form-data格式的数据需要引入boundary边界，该边界是一个不会在请求的其他地方出现的值，一般取一个随机字符串，假设为boundaryValue
  
   请求的格式 ：
     Content-Type: multipart/form-data; boundary= boundaryValue <br />
     Content-Length: (字节长度)<br />
     <br />
     \-\-boundaryValue<br />
     Content-Disposition: form-data; name="name"; filename="filename"
     Content-Type: image/png
     <br />
     <br /> 
     <文件的二进制数据,注意该数据上有两个换行><br/>
     \-\-boundaryValue<br />
     Content-Disposition: form-data; name="name"
     <br />
     <br />
     Value
     \-\-boundaryValue\-\- (后面需要接一个换行)
     <br />
     <br />
     *请求传输的数据用 \-\-boundaryValue 分割，每个 \-\-boundaryValue 下都会有一个 Content-Disposition: form-data; 以及相应的值，在插入值之前要先输入两个换行。所有数据结束时，使用\-\-boundaryValue\-\- + 换行表示结尾。*
     
#### 工单报修
  设备报修 ： 
  - 前台代码 TIT.ZNH.ZJSP.UI.RepairEditor <br / >
    其中故障类型的复选框数据来源来自 DmxCache (表：B_QJ_DMX )     
  - 后台代码 com.tit.znh.zj.sb.service.ServiceZJSB30 <br />
      ZJSBSbbx.xml
  - B_RS_DW ： 单位信息， DWNBBM 单位内部编码
  - 根据设备获取 dwnbbm，可以关联 B_SSSB_SBXX 和 B_RS_DW 得到，具体关联条件参照
     ZJSBSbxx.query

  - 数据插入运维表：
    - 工单表（a_mt_worksheet）
    - 工单设备表(a_mt_worksheet_device)
    - 工单故障表(a_mt_worksheet_faults)
  
  - 插入数据举例：
    - 工单表 : ID 生成方式: "MT-" + dateTime.toString("yyyyMMddHHmmssSSS"); <br /> CREATE_MODE 设置为2，表示该项目插入的数据；<br /> ext1 :设备所属的单位内部编码; <br /> ext4 : 工单的响应等级,默认undefined

    - 工单设备表
    - 工单故障表
  
  - sbbx表新增WorkSheetID字段，存储对应工单表ID

实现方式： POST 请求，提交json数据

第一屏：系统管理 -> 报修管理 跳转到扩展包项目ezViewExt
  http://localhost:8090/ezViewExt/faultreport/report.html

 
## 第二屏
#### 视频设备管理，必填项加\*
  进入方式： 第一屏 系统管理 -> 视频设备管理
  前端代码： TIT.ZNH.ZJSB.UI.VideoDeviceEdit.xaml.cs: IsValidInput()方法 添加有效性校验；<br />
  VideoDeviceEdit.xaml 增加\*
  
  摄像机位置类型、摄像机分辨率、摄像机朝向、摄像机型号、摄像机补光属性
    
#### 研判报告

修改外部服务axis2:ReportService类和CAManager类,
修改前台：ZJAJ.UI: CaseDetail.xaml.cs, ZJAJ80.xaml.cs, ZJAJ81.xaml.cs 
         ZJBG.UI: Common.cs, DataClass.cs, Delegate.cs, NewReportHandler.xaml,
                  NewReportHandler.xaml.cs, ReportDocument.xaml, ReportDocument.xaml.cs, CreateReport.xaml.cs 
    Main/ZNJT.WEB/ClientBin/ReportService.ClientConfig 配置外部服务路径
    ZJBG.UI.csproj 添加引用
数据库 B_TZ_ASJGL_AJGXR 添加字段用于存储结案信息

涉及表： B_TZ_ASJGL_YPBG, B_TZ_ASJGL_WDWJ, B_TZ_ASJGL_QZXX

QZLX的数据来源：m_DmxCache.GetDmxBlock(DmxCode.ASJGL_QZLX); 来源表B_QJ_DMX, B_QJ_DMLX

select * from B_QJ_DMLX where dmbm = 'ASJGL_QZLX';  # XH对应 B_QJ_DMX表DMLXXH
select * from B_QJ_DMX where DMLXXH = '22011';


#### 线索部门统计

 

