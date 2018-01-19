# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class RenrencheItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #城市
    city  = scrapy.Field()

    #城市链接
    #cityLink = scrapy.Field()

    #品牌
    brand = scrapy.Field()

    #车型
    carType = scrapy.Field()

    #车型年份
    carTypeYear = scrapy.Field()

    #车型配置
    carConfig = scrapy.Field()

    #购买年份
    buytime = scrapy.Field()

    #行驶里程
    mileage = scrapy.Field()

    #卖家报价
    price = scrapy.Field()

    #首付
    downPayment = scrapy.Field()
