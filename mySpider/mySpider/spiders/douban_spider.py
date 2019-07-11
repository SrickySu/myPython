# -*- coding: utf-8 -*-
import scrapy
from mySpider.items import MyspiderItem


class DoubanSpiderSpider(scrapy.Spider):
    name = 'douban_spider'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
        top25item = response.xpath("//div[@id='wrapper']//div[@class='item']")
        item = MyspiderItem()
        item['movieName'] = top25item[1].xpath(".//span[@class='title'][1]/text()").extract_first()
        item['star'] = top25item[1].xpath(".//span[@class='rating_num']/text()").extract_first()
        item['description'] = top25item[1].xpath(".//span[@class='inq']/text()").extract_first()
        yield item
