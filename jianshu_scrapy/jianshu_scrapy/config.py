MYSQL_HOST = '127.0.0.1'
MYSQL_DBNAME = 'jianshu_scrapy'        #数据库名字
MYSQL_USER = 'root'           #数据库账号
MYSQL_PASSWD = 'SYzCr2AZTIWMQYA3'         #数据库密码
MYSQL_PORT = 3306             #数据库端口
MYSQL_TABLE_NAME1 ='jianshu_users'    #数据库表名
MYSQL_TABLE_NAME2 ='jianshu_user_relation'    #数据库表名
base_headers = {'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4',
                'Accept-Encoding': 'gzip, deflate, sdch',
                'X-Requested-With': 'XMLHttpRequest',
                'Accept': 'text/html, */*; q=0.01',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
                'Connection': 'keep-alive',
                'Referer': 'http://www.baidu.com'}
timeout=10