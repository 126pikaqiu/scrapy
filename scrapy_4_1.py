import json
import time
import requests
# from fake_useragent import UserAgent
import random
import  myTools

# ua = UserAgent(verify_ssl=False)

# song_list = [{'186453':'春夏秋冬'},{'188204':'沉默是金'},{'188175':'倩女幽魂'},{'188489':'风继续吹'},{'187374':'我'},{'186760':'风雨起时'}]
song_list = ['186453','188204','188175','188489','187374','186760']

headers = {
    # 'Origin':'https://music.163.com',
    # 'Referer': 'https://music.163.com/song?id=26620756',
    # 'Host': 'music.163.com',
    'User-Agent': random.choice(myTools.my_tools_user_agents)
}

def get_comments(page,song_list):
    """
    :param page: 评论的第多少页，从0开始的
    :param ite: 歌单列表
    :return:
    """
    # 获取评论信息
    # """
    proxies = myTools.get_random_ip()
    print(proxies)
    for song_id in song_list:
        url = 'http://music.163.com/api/v1/resource/comments/R_SO_4_'+ song_id +'?limit=20&offset=' + str(page)
        try:
            response = requests.get(url=url, headers=headers,proxies = proxies)
        except Exception as e:
            print('Request error')
            continue
        # print(response.text)
        result = json.loads(response.text)
        items = result['comments']
        for item in items:
            # 用户名
            user_name = item['user']['nickname'].replace(',', '，')
            # 用户ID
            user_id = str(item['user']['userId'])
            # 评论内容
            comment = item['content'].strip().replace('\n', '').replace(',', '，')
            # 评论ID
            comment_id = str(item['commentId'])
            # 评论点赞数
            praise = str(item['likedCount'])
            # 评论时间
            date = time.localtime(int(str(item['time'])[:10]))
            date = time.strftime("%Y-%m-%d %H:%M:%S", date)
            print(user_name + ':' + comment)

if __name__ == '__main__':
    get_comments(0,song_list = song_list)

