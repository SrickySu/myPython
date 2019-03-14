#coding=utf-8
'''
Created on 2019年1月20日

@author: 74518
'''
import urllib2

class Downloader(object):
    def download(self, url):
        if url is None:
            return None 
        request = urllib2.Request(url)
        request.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36')
        request.add_header('Cookie', 'Hm_lvt_60bad21af9c824a4a0530d5dbf4357ca=1552563835; Hm_lvt_78c58f01938e4d85eaf619eae71b4ed1=1552563835; Hm_lvt_f79b64788a4e377c608617fba4c736e2=1552563835; Hm_lpvt_60bad21af9c824a4a0530d5dbf4357ca=1552576961; Hm_lpvt_f79b64788a4e377c608617fba4c736e2=1552576961; Hm_lpvt_78c58f01938e4d85eaf619eae71b4ed1=1552576961; v=At-tYgeg_xxZ9fsAEwDjWyCnbjhqRDOpTZo32nEteBrXavEueRTDNl1oxymC')
        request.add_header('Referer', url)
        response = urllib2.urlopen(request)
        if response.getcode() != 200:
            return None
        responseData = response.read()
        return responseData