"""
基于scrapy.spider.CrawlSpider的深度爬虫操作
"""

from scrapy.spiders import CrawlSpider,Rule

#引入链接提取模块
from scrapy.linkextractors import LinkExtractor
from ..items import ZhaopinItem

class ZhaopinSpider(CrawlSpider):
    name = 'zp'
    #limit domains
    allowed_domains = ["zhaopin.com"]
    #define start urls
    start_urls =[
        "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC%2b%E4%B8%8A%E6%B5%B7%2b%E5%B9%BF%E5%B7%9E%2b%E6%B7%B1%E5%9C%B3&kw=python&isadv=0&sg=7cd76e75888443e6b906df8f5cf121c1&p=1"
    ]
    #define the rules of extracting links
    link_extractor = LinkExtractor(
        allow=(r"e75888443e6b906df8f5cf121c1&p=\d+")
    )
    rules = [
        Rule(link_extractor,follow=True,callback='parse_response')
    ]

    # 处理响应数据
    def parse_response(self, response):
        # 提取当前页面所有需要的数据
        job_list = response.xpath("//div[@id='newlist_list_content_table']/table[position()>1]/tr[1]")
        for jobs in job_list:
            job = jobs.xpath("td[@class='zwmc']/div/a").xpath("string(.)").extract()[0]
            company = jobs.xpath("td[@class='gsmc']/a/text()").extract()[0]
            salary = jobs.xpath("td[@class='zwyx']/text()").extract()[0]
            print(job)
            print(company)
            print(salary)