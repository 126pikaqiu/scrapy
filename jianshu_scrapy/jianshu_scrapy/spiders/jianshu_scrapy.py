import scrapy
from scrapy import Request
from ..items import JianshuScrapyItem
from ..items import RelationItem
class jianshu_scrapy(scrapy.Spider):
    name = "jianshu"

    def start_requests(self):
        start_urls = [
            "http://www.jianshu.com/u/12532d36e4da",
            "http://www.jianshu.com/u/9b20c7d63b77",
            "http://www.jianshu.com/u/94bbc48171c7",
            "http://www.jianshu.com/u/181e7b1b1423",
            "http://www.jianshu.com/u/8faa58cbfde1",
            "http://www.jianshu.com/u/8530ab416e50"
        ]
        self.base_headers = {'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4',
                        'Accept-Encoding': 'gzip, deflate, sdch',
                        'X-Requested-With': 'XMLHttpRequest',
                        'Accept': 'text/html, */*; q=0.01',
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36',
                        'Connection': 'keep-alive',
                        'Referer': 'http://www.baidu.com'}
        for i in start_urls:
            yield scrapy.Request(i,headers=self.base_headers)

    def parse(self, response):
        item = JianshuScrapyItem()
        datas = response.css("div.meta-block p::text").extract()
        num_follower = datas[1]
        num_article = datas[2]
        num_like = datas[4]
        num_word = datas[3]
        num_following = datas[0]
        uid = response.css('div.title a.name::attr(href)').extract()[0][3:]
        nickname = response.css("div.title a.name::text").extract()[0]
        item['uid'] = uid
        item['nickname'] = nickname
        item['num_following'] = int(num_following)
        item['num_article'] = int(num_article)
        item['num_word'] = int(num_word)
        item['num_follower'] = int(num_follower)
        item['num_like'] = int(num_like)
        yield item
        yield Request("http://www.jianshu.com/users/{uid}/followers".format(uid=uid), headers=self.base_headers,
                      callback=self.parser_followers)
        # yield Request("http://www.jianshu.com/users/{uid}/following?page=1".format(uid=uid), headers=self.base_headers,
        #               callback=self.parser_followering)

    # def parser_followering(self, response):
    #     """
    #     filename=response.url.split('/')[-2]
    #     with open(filename,'wb') as f:
    #         f.write(response.body)
    #     #print ('+++++++++++++++++',response.status,'+++++++++++++++++++++')
    #     """
    #     author_uid = response.url.split('/')[-2]
    #     followers_per_page = 9
    #     followering_num = int(
    #         response.xpath('/html/body/div[1]/div/div[1]/ul/li[1]/a/text()').extract_first().split(' ')[-1])
    #     range_end = 10
    #     if followering_num < followers_per_page:
    #         range_end = followering_num
    #     for i in range(1, range_end):
    #         followering_uid = response.xpath(
    #             '/html/body/div[1]/div/div[1]/div[2]/ul/li[{id}]/div[1]/a/@href'.format(id=i)).extract_first().split(
    #             '/')[-1]
    #         yield Request("http://www.jianshu.com/u/{uid}".format(uid=followering_uid), headers=self.base_headers,
    #                       callback=self.parse)

    def parser_followers(self, response):
        """
            filename='followers.html'
            with open(filename,'wb') as f:
                f.write(response.body)
        """
        author_uid = response.url.split('/')[-2]
        # followers_per_page = 10
        followers_num = response.css("div.meta-block p::text")[2].extract()
        followers_num = int(followers_num)
        # page_num = int(followers_num) // followers_per_page

        range_end = 10
        if followers_num <= 9:
            range_end = followers_num
        for i in range(1, range_end):
            follower_uid = response.css("div.info a.name::attr(href)")[i - 1].extract().split('/')[-1]
            if follower_uid:
                return None
            yield Request("http://www.jianshu.com/u/{uid}".format(uid=follower_uid), headers=self.base_headers,
                          callback=self.parse)
            info_relation = RelationItem()
            info_relation['uid'] = author_uid
            info_relation['follower'] = follower_uid
            yield info_relation

        # if page_num >= 2:
        #     for i in range(2, page_num):
        #         url = 'http://www.jianshu.com/users/{uid}/followers?page={num}'.format(uid=author_uid, num=i)
        #         yield Request(url, headers=self.base_headers, callback=self.parser_followers_nextpage)

    # def parser_followers_nextpage(self, response):
    #     """
    #     print '+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
    #     filename='followers_nextpage.html'
    #     with open(filename,'wb') as f:
    #         f.write(response.body)
    #     """
    #     for i in range(1, 10):
    #         followers_path = '/html/body/div/div[1]/div[1]/div[2]/ul/li[{num}]/div[1]/a/@href'.format(num=i)
    #         result = response.xpath(followers_path).extract_first().split('/')
    #         # if result is not empty
    #         if len(result):
    #             followers_uid = result[-1]
    #             # print "http://www.jianshu.com/u/{uid}".format(uid=followers_uid)
    #             yield Request("http://www.jianshu.com/u/{uid}".format(uid=followers_uid), headers=self.base_headers,
    #                           callback=self.parse)




