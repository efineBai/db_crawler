# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from douban_crawler.items import MovieItem


def process_movie(item):

    pass


class DoubanCrawlerPipeline(object):
    def process_item(self, item, spider):
        if isinstance(item, MovieItem):
            process_movie(item)
        return item
