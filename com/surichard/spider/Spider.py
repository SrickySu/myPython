#coding=utf-8
'''
Created on 2019年1月20日

@author: 74518
'''
from com.surichard.spider import UrlManager, Downloader, UrlParser, OutputManager


class Spider(object):
    def __init__(self):
        self.urlManager = UrlManager.UrlManager()
        self.downloader = Downloader.Downloader()
        self.urlParser = UrlParser.UrlParser()
        self.outputManager = OutputManager.OutputManager()
    
    def craw(self, rootUrl):
        self.urlManager.addUrl(rootUrl)
        count = 1
        while self.urlManager.hasUrl():
            url = self.urlManager.getUrl()
            print count,':',url
            try:
                content = self.downloader.download(url)
                newUrls, data = self.urlParser.parse(url, content)
                self.urlManager.addUrls(newUrls)
                self.outputManager.collectData(data)
            except:
                print count,'craw failed'
            count += 1
            if count > 10:
                break
            
        self.outputManager.output()

spider = Spider()
rootUrl = 'https://baike.baidu.com/item/Python/407313'
spider.craw(rootUrl)
