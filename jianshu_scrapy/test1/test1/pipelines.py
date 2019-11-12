# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from .config import *
import pymysql

class Test1Pipeline(object):
    conn = pymysql.connect(MYSQL_HOST, MYSQL_USER, MYSQL_PASSWD, MYSQL_DBNAME)

    def __init__(self):
        try:
            self.cursor = self.conn.cursor()
            mysql = "create table if not exists {tablename} (uid varchar(20),author varchar (15),article varchar (20), num_read integer (6),num_comment integer (5)); ".format(
                tablename=MYSQL_TABLE_NAME1)
            self.cursor.execute(mysql)
            self.conn.commit()
            self.cursor.execute(mysql)
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()

    def process_item(self, item, spider):
        try:
            mysql = "insert into test_csdn_articles(uid,author,article, num_read,num_comment) values('%s','%s','%s',%d,%d); "%(item['uid'],item['author'],item['article'],int(item['num_read']),int(item['num_comment']))
            self.cursor.execute(mysql)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
        return item

    def close_spider(self,spider):
        self.conn.close()

    def open_spider(self,spider):
        pass
