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
        response = urllib2.urlopen(url)
        if response.getcode() != 200:
            return None
        responseData = response.read()
        return responseData