# -*- coding: utf-8 -*-
# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

import scrapy
from scrapy import http
from douban_crawler.items import MovieItem
import ast, json


class Db_Spider(scrapy.Spider):
    name = 'db_spider'
    allowed_domains = ['douban.com']
    start_urls = ['https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&'
                  'sort=recommend&page_limit=1&page_start=0']
    string = '悬疑'

    def parse(self, response):
        '''
        
        Args:
            response (http.Response): 

        Returns:
            
        '''
        subjects = response.body  # type:str

        print "response.body : ", isinstance(subjects, str), subjects.decode("utf-8", "igonre")
        if subjects is None :
            print "ERROR: subjects is none"
        subjects_array = json.loads(subjects)['subjects']

        for movie in subjects_array:
            print "movie : ", type(movie), movie
            request = scrapy.Request(url=movie[u'url'], callback=self.parse_movie_page)
            yield request

    def parse_movie_page(self, response):
        '''
        
        Args:
            response (http.Response): 
        Returns:

        '''
        info_list = response.xpath("//div[@id='info']")
        movie = MovieItem()
        movie['name'] = response.xpath("//span[@property='v:itemreviewed']/text()").extract()[0]
        print "movie : [%s]" % movie['name']
        movie['director'] = info_list.xpath(".//a[@rel='v:directedBy']/text()").extract()[0].encode("utf-8", "ignore")
        print "type(movie.director)", type(movie['director'])
        # //*[@id="info"]/span[3]/span[2]/span[2]/a
        movie['actors'] = [i.encode("utf8") for i in info_list.xpath("//a[@rel='v:starring']/text()").extract()]
        for i in movie['actors']:  # type:str
            print i.decode("utf-8")
        movie['category'] = [i.encode("utf8") for i in info_list.xpath("//span[@property='v:genre']/text()").extract()]
        for i in movie['category']:  # type:str
            print i.decode("utf-8")
        movie['country'] = info_list.xpath(u"//span[contains(text(), '制片国家')]/following-sibling::text()").extract()[0]  # type:unicode
        print "country= %s" % movie['country']
        movie['language'] = info_list.xpath(u"//span[contains(text(), '语言')]/following-sibling::text()").extract()[0]  # type:unicode
        print "language = %s" % movie['language']
        movie['date'] = info_list.xpath("//span[@property='v:initialReleaseDate']/text()").extract()[0]  # type:unicode
        print "date = ", movie['date']
        movie['length'] = info_list.xpath("//span[@property='v:runtime']/text()").extract()
        print "length = %s" % movie['length']
        movie['url'] = response.url
        movie['rate'] = response.xpath("//strong[@property='v:average']/text()").extract()
        print "rate = %s" % movie['rate']
        movie['rate_num'] = response.xpath("//span[@property='v:votes']/text()").extract()[0]
        print "rate_num = ", movie['rate_num']

