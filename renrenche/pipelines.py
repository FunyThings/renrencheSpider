# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import pymongo
from scrapy.conf import settings

class RenrenchePipeline(object):
    # def __init__(self):
    #     self.filename = open("renrenche.json", "w")
    #
    # def process_item(self, item, spider):
    #     text = json.dumps(dict(item), ensure_ascii=False) + ",\n"
    #     self.filename.write(text.encode("utf-8"))
    #     return item
    #
    # def close_spider(self, spider):
    #     self.filename.close()

    def __init__(self):
        #主机
        host = settings["MONGODB_HOST"]
        #端口
        port = settings["MONGODB_PORT"]
        #数据库
        dbname = settings["MONGODB_DBNAME"]
        #表
        sheetname = settings["MONGODB_SHEETNAME"]

        #创建mongoDB连接
        client = pymongo.MongoClient(host= host , port= port )

        #指定数据库
        mydb = client[dbname]

        #存放的数据库表名
        self.sheet = mydb[sheetname]


    def process_item(self, item ,spider):
        data = dict(item)
        self.sheet.insert(data)


        return item










