# -*- coding: utf-8 -*-
import scrapy
from scrapy_redis.spiders import RedisSpider

class SpbeenSpider(RedisSpider):
    name = 'spbeen'
    redis_key = 'url'
    # allowed_domains = ['spbeen.com']
    # start_urls = ['http://spbeen.com/']
    custom_settings = {
        'SCHEDULER': 'scrapy_redis.scheduler.Scheduler',
        'DUPEFILTER_CLASS': 'scrapy_redis.dupefilter.RFPDupeFilter',
        'REDIS_URL': 'redis://127.0.0.1:6379',

    }

    def parse(self, response):
        print(response.url,'**********')
        pass
