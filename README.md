# temperature-smog-detector-SOC

## 前言

### 这是我人生中第一次尝试独立设计一套片上系统(SOC)

从架构到电路再到代码全由自己一个人设计  

开始于

### 2020.2.16

## 蓝图

![](./pic/blueprint.PNG)

## 目录
* [前言](#前言)
* [蓝图](#蓝图)
* [概述](#概述)
* [系统架构](#系统架构)
* [电路设计](#电路设计)
* [程序设计](#程序设计)
    * [嵌入式程序](#嵌入式程序)
    * [服务器程序](#服务器程序)
    * [手机端程序](#手机端程序)
* [总结](#总结)
* [参考资料](#参考资料)
* [使用截图](#使用截图)

## 概述

### 系统需求

#### 基本需求

* 采集温度物理信号
- 将物理信号转换为数字信号
* 用LCD显示采集到的信号
- 最少每间隔100ms采集一次温度信号
* 手机通过无线网络获得实时温度数据
- 手机端与单片机每隔1秒钟至少传送一次温度信息

#### 扩展需求

* 采集烟雾物理信号
- 设计个人电脑可视化软件

### 开发环境

* os: Windows 10
- package: CC3200SDK v1.5.0
* IDE: Code Composer Studio 9.3.0
- Interpreter: Python 3.7
* IDE: Pycharm

### 开发工具

* CC3200 DEMO BOARD
- DH11 温度数字传感器

### 基本原理或技术

* SOC基本技术
- MySql8.0

### 实现功能

#### 基本功能

* 采集温度物理信号
- 将物理信号转换为数字信号
* 最少每间隔100ms采集一次温度信号
- 手机通过无线网络获得实时温度数据
* 手机端与单片机每隔1秒钟至少传送一次温度信息

#### 扩展功能

* 温度信息没有直接发送到手机上而是发送到网络上的服务器上先保存起来
- 服务器可以利用数据库软件对数据进行持久化操作
* 服务器可以用自身的算力对已经持久化的数据进行一定的数理统计和科学运算

#### 未实现功能

* 没有采集烟雾物理信号
- 没有用LCD显示采集到的信号

## 系统架构

## 电路设计

## 程序设计

### 嵌入式程序

### 服务器程序

#### http接口

##### 添加记录

###### 接口

    http://localhost/addInfo POST
    
###### JSON结构
    
    {
      "degree":"",
      "time":""
    }

SOC通过POST方式把新检测到的温度信息发送到服务器

##### 获取信息

###### 接口

    http://localhost/getInfo GET
    
###### JSON数组结构

    [
      {
        "degree":"",
      },
      {
        "degree":"",
      },
      {
        "degree":"",
      },
      ...
    ]
    
通过GET方式访问此接口获取服务器记录后统计完的温度信息

#### 数据库表结构







##### 温度信息表

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
    
每条从单片机上传来的温度信息对应产生表的一条记录。
    

### 手机端程序







## 总结

### 优点

* 轻量级
- 功耗低，占用网络带宽资源少

### 不足



### 困难

* 因为我的专业是网络工程所以一开始真的对嵌入式开发一无所知
- 一开始是打算用STC89 DEMO BOARD的，但是它并没有集成无线通信模块，需要通过串口通信，然后通过CC3200等SOC进行无线通信，既复杂又没有必要

### 收获



### 结语


 
## 参考资料

* https://visualgdb.com/tutorials/arm/cc3200/
- http://www.ti.com.cn/tool/cn/CC3200SDK

## 使用截图

