# 爬取网络小说

### 概述

娱乐所做，网络小说爬虫，能爬取目标网站一定量的网络小说
> 遵守robots协议

- 目标网站：http://www.shuquge.com/
- 数据库：sqlite3
- scrapy log level: INFO

### 运行

创建数据库的脚本已放至根目录，进入项目根目录，运行以下命令以创建数据库：

```
pip install scrapy
python createDatabases.py
```

在`spiders/spider.py`文件里的`start_requests`函数中设置目标范围，默认10000-10100, 然后运行以下命令启动爬虫:

```
scrapy crawl novel
```
> novel是spider/spider.py 文件中Spider类的name属性，可自定义

### 爬取速度

45分钟共爬取101篇小说，共计28959章

![](http://12138.site/static/contentImg/c2dcd4cb85d16086b59c7f9e7d9b769d.jpg)

![](http://12138.site/static/contentImg/be34e62157e717ef38e411bcf0c1ccb4.jpg)
