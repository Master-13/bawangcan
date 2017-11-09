# Readme
一键报名大众点评“霸王餐”所有（误，实际上是大部分）活动

## 系统需求
1. python  
2. selenium
3. Chrome>=60.x.x.x
4. Chromedriver  
>如果你没有安装Chromedriver或Chrome版本不正确，运行该脚本时会有下载地址提示。使用Chrome自带更新功能，请自行科学上网。


## 使用方法
首先用电脑访问大众点评霸王餐页面，登录你的账号，把`cookie`拷贝出来。仔细看，`cookie`里面有一个`dper`字段，把它的值作为脚本的参数运行就行了。
>如 python xxxxx.py d38baa6dbee1f081e4fd6c9a3eb6ca3d7b2ca7d9



## 更新 by Master_13
>@20171109
  
1. 只看还没有报名的  
2. 如果活动支持“黄金替补”，则会自动勾选  
3. 多商圈活动或多套餐活动自动忽略，请手工去网站上报名

## Original version
https://github.com/mascure/bawangcan

## 觉得好用，你为什么不Star
