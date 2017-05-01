# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanCrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

'''
            "rate": "7.9", 
            "cover_x": 1200, 
            "is_beetle_subject": false, 
            "title": "怒", 
            "url": "https://movie.douban.com/subject/26279289/", 
            "playable": false, 
            "cover": "https://img1.doubanio.com/view/movie_poster_cover/lpst/public/p2399174377.webp", 
            "id": "26279289", 
            "cover_y": 1698, 
            "is_new": false
'''


class MovieItem(scrapy.Item):

    name = scrapy.Field()
    rate = scrapy.Field()
    rate_num = scrapy.Field()
    url = scrapy.Field()
    director = scrapy.Field()
    actors = scrapy.Field()
    category = scrapy.Field()
    country = scrapy.Field()
    language = scrapy.Field()
    length = scrapy.Field()
    date = scrapy.Field()  # could be an array
    alias = scrapy.Field()


