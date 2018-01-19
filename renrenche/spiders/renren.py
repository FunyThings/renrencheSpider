# -*- coding: utf-8 -*-
import scrapy
import os
from renrenche.items import RenrencheItem
import sys

reload(sys)
sys.setdefaultencoding("utf-8")


class RenrenSpider(scrapy.Spider):
    name = 'renren'
    allowed_domains = ['renrenche.com']
    url = "https://www.renrenche.com/cn/ershouche/p"
    offset = 1
    start_urls = [url+str(offset)+"/"]

    def parse(self, response):

        # item = RenrencheItem()
        # item["city"] = response
        # yield item

        item = RenrencheItem()

        for each in response.xpath("//ul/li[@class='span6 list-item car-item']/a[@rrc-event-param='search']"):

            #所在城市
            item["city"] = each.xpath("./div[@class='img-backgound']/div[@class='position-bg']/span/text()").extract()[0]

            try:
                #品牌
                item["brand"] = each.xpath("./h3/text()").extract()[0].split(" ")[0].split("-")[0]
                #车型
                item["carType"] = each.xpath("./h3/text()").extract()[0].split(" ")[0].split("-")[1]

            except:
                item["brand"] = each.xpath("./h3/text()").extract()[0]
                item["carType"] = each.xpath("./h3/text()").extract()[0]

            #车型年份
            item["carTypeYear"] = each.xpath("./h3/text()").extract()[0].split(" ")[1]

            #车型配置
            carconfig_list = each.xpath("./h3/text()").extract()[0].split(" ")[2:]
            carconfig = ' '.join(carconfig_list)
            item["carConfig"] = carconfig

            #购买年份
            item["buytime"] = each.xpath("./div[@class='mileage']/span[@class='basic']/text()").extract()[0]

            #行驶里程
            item["mileage"] = each.xpath("./div[@class='mileage']/span[@class='basic']/text()").extract()[1]

            #价格
            item["price"] = each.xpath("./div[@class='tags-box']/div[@class='price']/text()").extract()[0].strip()

            #首付
            try:
                payment = each.xpath( "./div[@class='tags-box']/div[@class='price']/div[@class='down-payment']/div[@class='m-l']/text()").extract()[0]
                item["downPayment"] = payment
            except:
                item["downPayment"] = 0

            yield  item



        if self.offset < 175 :
             self.offset += 1

             yield scrapy.Request(url="https://www.renrenche.com/cn/ershouche/p" + str(self.offset) + "/", callback= self.parse ,dont_filter=True)



