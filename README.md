# bawangcan
自动报名大众点评霸王餐，将报名所有霸王餐和休闲娱乐的同城活动

#先决条件
1、mac系统  
2、安装了chrome浏览器

#用法
1、获取点评的cookie：以chrome为例，浏览器登陆一次点评，然后设置-》内容设置-》所有cookie和网站数据，搜索dianping.com，点dper，会得到dper这个cookie的详细信息，复制‘内容’后面的字符串，记下来。

2、下载bin下的bawangcan文件，在terminal运行以下命令(将$dper替换为刚才复制的字符串)：  
`./bawangcan $dper`

3、报名成功

#其他
源码在src下面，如果本地有Python环境且安装了selenium，也可以用以下命令：  
`python bawangcan.py $dper`
