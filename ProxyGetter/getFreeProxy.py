# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     getFreeProxy.py  
   Description :  抓取免费代理
   Author :       JHao
   date：          2016/11/25
-------------------------------------------------
   Change Activity:
                   2016/11/25: 
-------------------------------------------------
"""
import re
import sys
import requests

reload(sys)
sys.setdefaultencoding('utf-8')

from Util.utilFunction import robustCrawl, getHtmlTree


# 快代理
@robustCrawl
def freeProxyFirst(page=10):
    """
    抓取快代理IP http://www.kuaidaili.com/
    :param page: 翻页数
    :return:
    """
    url_list = ('http://www.kuaidaili.com/proxylist/{page}/'.format(page=page) for page in range(1, page + 1))
    # 页数不用太多， 后面的全是历史IP， 可用性不高
    for url in url_list:
        tree = getHtmlTree(url)
        proxy_list = tree.xpath('.//div[@id="index_free_list"]//tbody/tr')
        for proxy in proxy_list:
            yield ':'.join(proxy.xpath('./td/text()')[0:2])


# 代理66
@robustCrawl
def freeProxySecond(proxy_number=100):
    """
    抓取代理66 http://www.66ip.cn/
    :param proxy_number: 代理数量
    :return:
    """
    url = "http://m.66ip.cn/mo.php?sxb=&tqsl={}&port=&export=&ktip=&sxa=&submit=%CC%E1++%C8%A1&textarea=".format(
            proxy_number)
    html = requests.get(url).content
    for proxy in re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,4}', html):
        yield proxy


# 有代理
@robustCrawl
def freeProxyThird(days=1):
    """
    抓取有代理 http://www.youdaili.net/Daili/http/
    :param days:
    :return:
    """
    url = "http://www.youdaili.net/Daili/http/"
    tree = getHtmlTree(url)
    page_url_list = tree.xpath('.//div[@class="chunlist"]/ul//a/@href')[0:days]
    for page_url in page_url_list:
        html = requests.get(page_url).content
        proxy_list = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,4}', html)
        for proxy in proxy_list:
            yield proxy


# 西刺
@robustCrawl
def freeProxyFourth():
    """
    抓取西刺代理 http://api.xicidaili.com/free2016.txt
    :return:
    """
    url = "http://api.xicidaili.com/free2016.txt"
    html = requests.get(url).content
    for proxy in re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,4}', html):
        yield proxy


# guobanjia
@robustCrawl
def freeProxyFifth():
    """
    抓取guobanjia http://www.goubanjia.com/free/gngn/index.shtml
    :return:
    """
    url = "http://www.goubanjia.com/free/gngn/index.shtml"
    tree = getHtmlTree(url)
    proxy_list = tree.xpath('.//td[@class="ip"]')
    for proxy in proxy_list:
        yield ''.join(proxy.xpath('.//text()'))


if __name__ == '__main__':
    for e in freeProxyFifth():
        print e