# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from .items import JianshuScrapyItem
from .config import *
import pymysql
from .items import RelationItem


class JianshuScrapyPipeline(object):
    conn = pymysql.connect(MYSQL_HOST, MYSQL_USER, MYSQL_PASSWD, MYSQL_DBNAME)
    def __init__(self):
        try:
            # self.conn = pymysql.connect(MYSQL_HOST, MYSQL_USER, MYSQL_PASSWD, MYSQL_DBNAME)
            self.cursor = self.conn.cursor()
            mysql = "create table if not exists {tablename} (uid varchar(20),nickname varchar (30),following_num integer (5),follower_num integer (7),articles_num integer (6),words_num integer (10),beliked_num integer (5)); ".format(
                tablename=MYSQL_TABLE_NAME1)
            self.cursor.execute(mysql)
            self.conn.commit()
            mysql = "create table if not exists {tablename} ( uid varchar(20),follower_uid varchar (20)); ".format(
                tablename=MYSQL_TABLE_NAME2)
            self.cursor.execute(mysql)
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()

    def item_a_insert(self, item):
        try:
            mysql = "insert into jianshu_users(uid,nickname,following_num,follower_num,articles_num,words_num,beliked_num) values('%s','%s',%d,%d,%d,%d,%d); "%(item['uid'],item['nickname'],int(item['num_following']),int(item['num_follower']),int(item['num_article']),int(item['num_word']),int(item['num_like']))
            self.cursor.execute(mysql)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()

    def item_b_insert(self, item):
        try:
            mysql = "insert into jianshu_user_relation(uid,follower_uid) values ('%s','%s');"%(item['uid'], item['follower'])
            self.cursor.execute(mysql)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()

    def process_item(self, item, spider):
        if isinstance(item, JianshuScrapyItem):
            self.item_a_insert(item)
        if isinstance(item, RelationItem):
            print("relationitem------------------------------------------------------")
            self.item_b_insert(item)
        return item

    def close_spider(self,spider):
        self.conn.close()

    def open_spider(self,spider):
        pass
