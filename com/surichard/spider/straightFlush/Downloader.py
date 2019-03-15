#coding=utf-8
'''
Created on 2019年1月20日

@author: 74518
'''
import urllib2, cookielib

class Downloader(object):
    cookieStr = 'Hm_lvt_60bad21af9c824a4a0530d5dbf4357ca=1552563835,1552582429; Hm_lvt_78c58f01938e4d85eaf619eae71b4ed1=1552563835,1552582429; Hm_lvt_f79b64788a4e377c608617fba4c736e2=1552563835,1552582429; Hm_lpvt_60bad21af9c824a4a0530d5dbf4357ca=1552583111; Hm_lpvt_78c58f01938e4d85eaf619eae71b4ed1=1552583111; Hm_lpvt_f79b64788a4e377c608617fba4c736e2=1552583111; v=Atelek-YR6T2pcMokOFrsxgfZkAiHKsthfEv7ykG8X4Pevk2Mew7zpXAv0A6'
    def download(self, rootUrl, url, startFlag):
        if url is None:
            return None 
        cookie = cookielib.CookieJar()
        handler = urllib2.HTTPCookieProcessor(cookie)
        opener = urllib2.build_opener(handler)
        
        request = urllib2.Request(url)
        request.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36')
        if startFlag:
            request.add_header('Upgrade-Insecure-Requests', '1')
        else:
            #request.add_header('Accept', 'text/html, */*; q=0.01')
            #request.add_header('Referer', rootUrl)
            #request.add_header('X-Requested-With', 'XMLHttpRequest')
            #request.add_header('hexin-v', 'Ahxu9pCErKTd8Vh4mMTVipfW7THNlcSCQj_Ui_YdK4vr0bZnHqWQT5JJpBVF')
            request.add_header('Connection', 'keep-alive')
            request.add_header('Host', 'data.10jqka.com.cn')
            request.add_header('Upgrade-Insecure-Requests', '1')
            request.add_header('Cookie', 'Hm_lvt_60bad21af9c824a4a0530d5dbf4357ca=1552550847,1552624108; Hm_lpvt_60bad21af9c824a4a0530d5dbf4357ca=1552624108; Hm_lvt_f79b64788a4e377c608617fba4c736e2=1552550847,1552624108; Hm_lpvt_f79b64788a4e377c608617fba4c736e2=1552624108; Hm_lvt_78c58f01938e4d85eaf619eae71b4ed1=1552550847,1552624108; Hm_lpvt_78c58f01938e4d85eaf619eae71b4ed1=1552624108; v=As-9Tyclz02ThMsxkgZWkzgHXmja9CMWvUgnCuHcaz5FsOUe6cSzZs0Yt1vy')
        response = opener.open(request)
        if len(cookie) > 0:
            #self.cookieStr = ''
            for item in cookie:
                self.cookieStr = item.name + '=' + item.value
            print 'cookieStr =', self.cookieStr
        if response.getcode() != 200:
            return None
        responseData = response.read()
        return responseData