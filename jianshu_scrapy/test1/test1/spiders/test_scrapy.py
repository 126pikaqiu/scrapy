import scrapy
from ..items import Test1Item
class test_spider(scrapy.spiders.Spider):
    name = "csdn"
    start_urls = ["https://www.csdn.net/nav/career"]

    def parse(self,response):
        article_list = response.css("div.title h2 a::text").extract()
        author_list = response.css("dd.name a::text").extract()
        num_read_list = response.css("dd.read_num a span.num::text").extract()
        num_comment_list = response.css("dd.common_num a span.num::text").extract()
        uid_list = response.css("dd.common_num a::attr(href)").extract()
        # num_pages = len(article_list) // 18
        for i in range(17):
            info_item = Test1Item()
            info_item["article"] = article_list[i].strip('\n').strip()
            info_item['author'] = author_list[i].strip('\n').strip()
            info_item['num_read'] = int(num_read_list[i])
            info_item['num_comment'] = int(num_comment_list[i])
            info_item['uid'] = uid_list[i].split('/')[-4]
            yield info_item
        # for i in range(num_pages):
        #     yield scrapy.Request(self.start_urls[0],callback=self.parse)




