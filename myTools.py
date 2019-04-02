# IP地址取自国内髙匿代理IP网站：http://www.xicidaili.com/nn/
# 仅仅爬取首页IP地址就足够一般使用

from bs4 import BeautifulSoup
import requests
import random
ip_list_url = 'https://www.xicidaili.com/nt/2'

my_tools_user_agents = [
    'Opera/9.25 (Windows NT 5.1; U; en)',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
    'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
    'Mozilla/5.0 (X11; U; linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
    'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9'
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
]

# def getHTMLText(url,proxies):
#     try:
#         r = requests.get(url,proxies=proxies)
#         r.raise_for_status()
#         r.encoding = r.apparent_encoding
#     except:
#         return 0
#     else:
#         return r.text

def get_random_agent():
    """
    获得随机代理
    :return:
    """
    return random.choice(my_tools_user_agents)

def get_random_ip():
    """
    获得随机代理ip
    :return:
    """
    my_tools_headers = {'User-Agent': random.choice(my_tools_user_agents)}
    web_data = requests.get(url = ip_list_url,headers = my_tools_headers)
    soup = BeautifulSoup(web_data.text, 'html.parser')
    ips = soup.find_all('tr')
    ip_list = []
    for i in range(1, len(ips)):
        ip_info = ips[i]
        tds = ip_info.find_all('td')
        ip_content = tds[5].text + '://' + tds[1].text + ':' + tds[2].text
        ip_list.append(ip_content)
    #检测ip可用性，移除不可用ip：（这里其实总会出问题，你移除的ip可能只是暂时不能用，剩下的ip使用一次后可能之后也未必能用）
    for ip in ip_list:
        try:
            proxy_temp = {"http": ip}
            res = requests.get(url = ip_list_url, headers = my_tools_headers,proxies = proxy_temp)
            return proxy_temp
        except Exception as e:
            ip_list.remove(ip)
    return []

def refresh(text):
    return text.replace('<br>','\n')

# def get_random_ip(ip_list):
#     """
#     :param ip_list: 一堆可用的代理ip
#     :return:
#     """
#     proxy_list = []
#     for ip in ip_list:
#         proxy_list.append(ip)
#     proxy_ip = random.choice(proxy_list)
#     proxies = {'http': proxy_ip}
#     return proxies
# ---------------------
# 作者：睡着的月亮
# 来源：CSDN
# 原文：https://blog.csdn.net/weixin_40372371/article/details/80154707
# 版权声明：本文为博主原创文章，转载请附上博文链接！