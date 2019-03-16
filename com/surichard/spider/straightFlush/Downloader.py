#coding=utf-8
'''
Created on 2019年1月20日

@author: 74518
'''
import urllib2, cookielib, random

class Downloader(object):
    initCookieStr = 'Hm_lvt_60bad21af9c824a4a0530d5dbf4357ca=1552563835,1552582429; Hm_lvt_78c58f01938e4d85eaf619eae71b4ed1=1552563835,1552582429; Hm_lvt_f79b64788a4e377c608617fba4c736e2=1552563835,1552582429; Hm_lpvt_60bad21af9c824a4a0530d5dbf4357ca=1552583111; Hm_lpvt_78c58f01938e4d85eaf619eae71b4ed1=1552583111; Hm_lpvt_f79b64788a4e377c608617fba4c736e2=1552583111; v=Atelek-YR6T2pcMokOFrsxgfZkAiHKsthfEv7ykG8X4Pevk2Mew7zpXAv0A6'
    cookieStr = initCookieStr
    userAgent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    user_agents = [
                    'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
                    'Opera/9.25 (Windows NT 5.1; U; en)',
                    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
                    'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
                    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
                    'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9',
                    "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77 Safari/535.7",
                    "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0 ",
 
                    ]
    def download(self, rootUrl, url, startFlag, urlParser):
        if url is None:
            return None 
        cookie = cookielib.CookieJar()
        handler = urllib2.HTTPCookieProcessor(cookie)
        opener = urllib2.build_opener(handler)
        
        request = urllib2.Request(url)
        
        if urlParser.tryTime != urlParser.initTryTime:
            index = random.randint(0, 7)
            self.userAgent = self.user_agents[index]
            
        request.add_header('User-Agent', self.userAgent)
        
        if startFlag:
            request.add_header('Upgrade-Insecure-Requests', '1')
        else:
            #request.add_header('Accept', 'text/html, */*; q=0.01')
            request.add_header('Referer', rootUrl)
            #request.add_header('X-Requested-With', 'XMLHttpRequest')
            #request.add_header('hexin-v', 'Ahxu9pCErKTd8Vh4mMTVipfW7THNlcSCQj_Ui_YdK4vr0bZnHqWQT5JJpBVF')
            request.add_header('Connection', 'keep-alive')
            request.add_header('Host', 'data.10jqka.com.cn')
            #request.add_header('Upgrade-Insecure-Requests', '1')
            request.add_header('Cookie', self.cookieStr)
        response = opener.open(request)
        if len(cookie) > 0:
            #self.cookieStr = ''
            for item in cookie:
                self.cookieStr = item.name + '=' + item.value + '; ' + self.cookieStr
        else:
            index = random.randint(0, 7)
            self.userAgent = self.user_agents[index]
            self.cookieStr = self.initCookieStr
        if response.getcode() != 200:
            return None
        responseData = response.read()
        return responseData