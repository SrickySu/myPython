#coding=utf-8
'''
Created on 2019年1月20日

@author: 74518
'''
from com.surichard.spider import UrlManager, Downloader
import UrlParser, OutputManager

class Spider(object):
    def __init__(self):
        self.urlManager = UrlManager.UrlManager()
        self.downloader = Downloader.Downloader()
        self.urlParser = UrlParser.UrlParser()
        self.outputManager = OutputManager.OutputManager()
    
    def craw(self, rootUrl):
        self.urlManager.addUrl(rootUrl)
        while self.urlManager.hasUrl():
            url = self.urlManager.getUrl()
            try:
                content = self.downloader.download(url)
                newUrl, data = self.urlParser.parse(content)
                self.urlManager.addUrl(newUrl)
                self.outputManager.collectData(data)
            except:
                print 'craw failed'
            
        self.outputManager.output()

spider = Spider()
rootUrl = 'http://data.10jqka.com.cn/hgt/hgtb/'
spider.craw(rootUrl)
