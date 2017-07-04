# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy.conf import settings
from scrapy.contrib.pipeline.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy.http import Request

class QunarspiderPipeline(object):

    def __init__(self):
        self.server = settings['MONGODB_SERVER']
        self.port = settings['MONGODB_PORT']
        # 数据库登录需要帐号密码的话
        # self.client.admin.authenticate(settings['MINGO_USER'], settings['MONGO_PSW'])
        self.db = settings["MONGODB_DB"]
        self.coll = settings["MONGO_DB_COLLECTTION"]
        client = pymongo.MongoClient(self.server,self.port)
        db = client[self.db]
        self.collection = db[self.coll]

    def process_item(self, item, spider):
        postItem = dict(item)
        self.collection.insert(postItem)
        return item

class ArticleImagePipeline(ImagesPipeline):
    def process_item(self, item, spider):
        return item