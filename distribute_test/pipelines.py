# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import redis

class DistributeTestPipeline(object):

    def __init__(self):
        self.r = redis.StrictRedis(host='localhost',port=6379,db=0)


    def process_item(self, item, spider):

        self.r.rpush('url',item['url'])
        return item
