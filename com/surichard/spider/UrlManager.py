#coding=utf-8
'''
Created on 2019年1月20日

@author: 74518
'''
class UrlManager(object):
    def __init__(self):
        self.newUrlSet = set()
        self.oldUrlSet = set()
        
    def addUrl(self, url):
        if url is None:
            return
        if url not in self.newUrlSet and url not in self.oldUrlSet:
            self.newUrlSet.add(url)
            
    def addUrls(self, urls):
        if urls is None:
            return
        for url in urls:
            self.addUrl(url)
            
    def hasUrl(self):
        return len(self.newUrlSet) != 0
    
    def getUrl(self):
        url = self.newUrlSet.pop()
        self.oldUrlSet.add(url)
        return url
            