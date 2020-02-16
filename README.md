# temperature-smog-detector-SOC

## 前言

### 这是我人生中第一次尝试独立设计一套片上系统

从架构到电路再到代码全由自己一个人设计  

开始于

### 2020.2.16

## 蓝图

![](./pic/blueprint.PNG)

## 目录
* [前言](#前言)
* [概述](#概述)
* [系统架构](#系统架构)
* [电路设计](#电路设计)
* [程序设计](#程序设计)
    * [51单片机](#51单片机)
* [总结](#总结)
* [参考资料](#参考资料)
* [软件截图](#软件截图)

## 概述

### 系统需求

#### 基本需求

* 采集烟雾和温度两种物理信号
- 将物理信号转换为数字信号
* 用LCD显示采集到的信号
- 最少每间隔100ms采集一次温度信号
* 手机通过无线网络获得实时温度数据
- 手机端与单片机每隔1秒钟至少传送一次温度信息

#### 扩展需求

* 设计个人电脑可视化软件

### 开发环境

* os: Windows 10  
- IDE: Code Composer Studio 9.3.0

### 开发工具

* STC89/STC12 DEMO BOARD v4.3 51单片机开发板
- DH11 温度数字传感器

### 基本原理或技术

* Spring boot
- JDBC
* MySql8.0

### 实现功能

#### 基本功能

* 寝室分配
- 学生管理
* 信息查询

#### 扩展功能

* 出入登记
- 前后端分离
* 具有简洁友好的用户界面
- 具有区分特权用户和普通用户的功能

#### 未实现功能

* 没有给每个表都做全增删查改的功能

## 数据库概念结构

### E-R图

![](./pic/2.PNG)

## 程序概要设计

### 程序架构

![](./pic/1.PNG)

## 程序详细设计

### 表结构Sql摘录

#### 学生表

    create table student
    (
      count int auto_increment,
      studentID varchar(45) null,
      college varchar(45) null,
      bedID varchar(45) null,
      name varchar(45) null,
      date1 varchar(45) null,
      date2 varchar(45) null,
      live boolean null,
      politics varchar(45) null,
      sex varchar(45) null,
      `desc` varchar(300) null,
      constraint student_pk
        primary key (count)
    );
    
每个入学的学生对应产生表的一条记录。
    
#### 床表

    create table bed
    (
      count int auto_increment,
      bedID varchar(45) null,
      buildingID varchar(45) null,
      can boolean null,
      constraint bed_pk
        primary key (count)
    );

学校的每张床对应表的一条记录

### 重要库

#### JDBC操作库

    import java.sql.*;
    
#### 编码JSON库

    import java.util.Map;
    import java.util.LinkedHashMap;
    import org.json.JSONObject;
    import org.json.JSONArray;

#### Http接收和响应库

    import org.springframework.web.bind.annotation.RestController;
    import org.springframework.web.bind.annotation.GetMapping;
    import org.springframework.web.bind.annotation.PostMapping;
    import org.springframework.web.bind.annotation.RequestBody;
    
### http接口摘录

#### 学生类

    http://localhost/addStudent POST

通过POST方式把新学生的数据序列化以JSON的形式发到这个接口上来实现增加学生功能，会返回一个JSON数据告知用户端是否操作成功。

    http://localhost/deleteStudent POST

通过POST方式把所要删除的学生的序号序列化以JSON的形式发到这个接口上来实现删除学生功能，会返回一个JSON数据告知客户端是否操作成功。   
        
    http://localhost/student GET
    
通过GET方式访问这个接口会返回一个包含所有学生的JSON Array。 

#### 床类

    http://localhost/canUseBed POST

通过POST方式把需要查询的床号序列化成JSON发送到服务器，服务器会返回一个JSON数据告知客户端查询的床能不能用。

    http://localhost/studentAddBed POST

通过POST方式把需要分配床的学的学生信息和床号序列化以JSON的形式发送到服务器，服务器会返回一个JSON数据告知客户端分配是否成功。

### JSON结构

#### 温度信息

    {
      "state":"",
      "degree":"",
      "timestamp":""
    }

## 总结

### 优点

* 运用了课堂上没有教学的前端框架vue.js和element UI

### 不足



### 困难

* 因为我的专业是网络工程所以一开始真的对嵌入式开发一无所知
- 一开始是打算用STC89 DEMO BOARD的，但是它并没有集成无线通信模块，需要通过串口通信，然后通过CC3200等SOC进行无线通信，既复杂又没有必要

### 收获



### 结语


 
## 参考资料

* https://visualgdb.com/tutorials/arm/cc3200/
- http://www.ti.com.cn/tool/cn/CC3200SDK

## 软件截图

