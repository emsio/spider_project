# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import scrapy
from itemadapter import ItemAdapter


class JianzhijobPipeline:
    ####处理yield传递过来的item
    def process_item(self, item,response:scrapy.http.response):
        ###spider是传递item的爬虫任务对象
        # print('JianzhijobPipeline=>process_item()',item)
        item['title'] = response.xpath('//title/text()').extract()
        item['price'] = response.xpath('//span[@class="job_price"]/text()').extract()
        yield  item
        return item
