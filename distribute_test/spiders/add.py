# -*- coding: utf-8 -*-
import scrapy
import time

class AddSpider(scrapy.Spider):
    name = 'add'
    allowed_domains = ['spbeen.com']
    start_urls = ['http://spbeen.com/']
    custom_settings = {'ITEM_PIPELINES':
            {
              'distribute_test.pipelines.DistributeTestPipeline': 300,
            }
        }

    def parse(self,response):
        item = {}
        for i in range(1000):
            item['url'] = 'http://spbeen.com'
            yield item
            time.sleep(0.5)

