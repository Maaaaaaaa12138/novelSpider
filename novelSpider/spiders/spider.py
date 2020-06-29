import scrapy
from novelSpider.items import *

class Spider(scrapy.Spider):

    name = "novel"

    def start_requests(self):
        "开始请求"
        for i in range(10000, 10101):
            url = f"http://www.shuquge.com/txt/{i}/index.html"
            yield scrapy.Request(url, meta={"id": i})
    
    def parse(self, response):
        "获取章节列表"
        getInfo = lambda x: x.split("：")[1]
        chapterList = response.xpath("//div[@class='listmain']/dl/dd/a")
        titles = chapterList.xpath("text()").extract()      # 标题列表
        urls = chapterList.xpath("@href").extract()         # 链接列表
        ID = response.meta.get("id")
        infos = response.xpath("//div[@class='small']/span/text()").extract()
        author = getInfo(infos[0])  # 作者
        type_ = getInfo(infos[2])   # 状态
        name = response.xpath("//h2/text()").extract()[0]
        chapterIDs = [i.split(".")[0] for i in urls]
        urls = [f"http://www.shuquge.com/txt/{ID}/{i}" for i in urls]
        yield novelItem(ID=ID, NAME=name, AUTHOR=author, TYPE=type_)
        for url, title, chapterId in zip(urls, titles, chapterIDs):
            yield scrapy.Request(url, self.getContent, meta={"title": title, "novelId": ID, "chapterId": chapterId})
    
    def getContent(self, response):
        "获取章节正文"
        content = "".join(response.xpath("//div[@id='content']/text()").extract())
        title = response.meta.get("title")
        novelId = response.meta.get("novelId")
        id = response.meta.get("chapterId")
        return NovelspiderItem(id=id, title=title, content=content, novelId=novelId)
