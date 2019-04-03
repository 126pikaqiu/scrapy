import scrapy

class MySpider(scrapy.spiders.Spider):
    """
启动程序的命令 scrapy runspider scrapyer_4_2.py非项目级
scrapy crawl <spidername> 项目级
    """
    #爬虫的名字
    name = 'spiderDaZhongShi'
    #爬取的小说首页
    start_urls = ['http://bbs.tianya.cn/post-16-1126849-1.shtml']

    #主要的函数
    def parse(self,response):
        content = []
        for i in response.xpath("//div"):
            #作者蛇从革的天涯帐号
            if i.xpath('@_hostid').extract() == ['13357319']:
                for j in i.xpath('div//div'):
                    #提取文本
                    c = j.xpath('text()').extract()
                    #过滤干扰符号
                    g = lambda x:x.strip('\n\r\u3000').replace('<br>','\n').replace('|','')
                    c = '\n'.join(map(g,c)).strip()
                    content.append(c)
                    with open('result.txt','a+',encoding='utf8') as fp:
                        fp.writelines(content)

                    #获取下一页网址继续爬取
                    url = response.url
                    d = url[url.rfind('-') + 1:url.rfind('.')]
                    next_url = 'http://bbs.tianya.cn/post-16-1126849-{0}.shtml'.format(int(d) + 1)
                    try:
                        yield scrapy.Request(url=next_url,callback=self.parse)
                    except:
                        pass