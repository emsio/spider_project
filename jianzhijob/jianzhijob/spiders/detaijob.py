import scrapy
# from jianzhijob.jianzhijob.jianzhijob.items import JianzhijobItem
# from jianzhijob.jianzhijob.jianzhijob.items import JianzhijobItem


class DetaijobSpider(scrapy.Spider):
    name = 'detaijob'
    allowed_domains = ['jianzhimao.com']
    start_urls = ['https://beijing.jianzhimao.com/']

    def parse(self, response:scrapy.http.response):
        # item = JianzhijobItem()
        print(response.body)
        print(response.url)
        print(response.request.url)
        print(response.headers)
        print(response.request.headers)
        print(response.status)
        print(response.xpath('//*[@id="content_list_wrap"]/li[2]/a').extract())
        pass


        # item['title'] = response.xpath('//title/text()').extract()
        # item['price'] = response.xpath('//span[@class="job_price"]/text()').extract()
        # yield  item
