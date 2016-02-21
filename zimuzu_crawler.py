#! /usr/bin/env python
# -*- coding:utf-8 -*-

import urllib
import urllib2
import cookielib
from bs4 import BeautifulSoup

# 抓取zimuzu.tv美剧下载地址
#
# by leohuachao


# 登陆地址
LOGIN_URL = "http://www.zimuzu.tv/User/Login/ajaxLogin"

def login(username, password):
    cookie = cookielib.MozillaCookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    post_data = urllib.urlencode({
                'account': username,
                'password': password,
                'remember': '1',
            })
    result = opener.open(LOGIN_URL, post_data)
    return opener

def crawl_url(opener, url, season, format, type):
    html = opener.open(url).read()
    soup = BeautifulSoup(html, "html.parser")
    lis = soup.find_all("li", attrs={'class':'clearfix', 'format':format, 'season':season})
    return [li.find("div", attrs={'class':'fr'}).find("a", attrs={'type':type})['href'] for li in lis]
   
if __name__ == "__main__":
    tv_url = "http://www.zimuzu.tv/resource/list/11057"
    season = 4
    format = "HR-HDTV"
    type = "ed2k"

    username = raw_input("input username:")
    password = raw_input("input password:")

    # 登录
    opener = login(username, password)

    download_urls = crawl_url(opener, tv_url, season, format, type)
    for url in download_urls:
        print url
