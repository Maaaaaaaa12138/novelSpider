# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3

class NovelspiderPipeline:

    def __init__(self):
        self.db = sqlite3.connect("novel.db")
        self.cursor = self.db.cursor()
        super().__init__()

    def process_novel(self, item):
        '向数据库中存入小说'
        ID = item.get("ID")
        NAME = item.get("NAME")
        AUTHOR = item.get("AUTHOR")
        TYPE = item.get("TYPE")
        self.cursor.execute(f"insert into novel values({ID}, '{NAME}', '{AUTHOR}', '{TYPE}')")
        
    def process_chapter(self, item):
        '向数据库中存入章节'
        title = item.get("title")
        content = item.get("content")
        novelId = item.get("novelId")
        id = item.get("id")
        self.cursor.execute(f"insert into chapter values(?, ?, ?, ?)", (id, title, content, novelId))


    def process_item(self, item, spider):
        '将数据存入数据库'
        if item.get("NAME"):
            self.process_novel(item)
        else:
            self.process_chapter(item)
        
        # 数据库提交
        self.db.commit()    
        return item
