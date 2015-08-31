# -*- coding: utf-8 -*-
import scrapy


class Hao123Spider(scrapy.Spider):
    name = "hao123"
    allowed_domains = ["hao123.com"]
    start_urls = (
        'http://www.hao123.com/',
    )

    def parse(self, response):
        pass
