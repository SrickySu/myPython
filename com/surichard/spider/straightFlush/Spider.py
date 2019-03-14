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
    
    def craw(self, rootUrl, header, fileName):
        self.urlManager.addUrl(rootUrl)
        self.outputManager.collectData(header)
        while self.urlManager.hasUrl():
            url = self.urlManager.getUrl()
            try:
                content = self.downloader.download(url)
                newUrl, data = self.urlParser.parse(url, content)
                self.urlManager.addUrl(newUrl)
                self.outputManager.collectData(data)
            except:
                print 'craw failed'
                self.outputManager.output(fileName)
            
        #self.outputManager.output()

spider = Spider()
rootUrl = 'http://data.10jqka.com.cn/hgt/ggtb/'
header = {}
header[0] = u'日期'
header[1] = u'当日资金流入(港元)'
fileName = u'港股通(沪)_最近一月.txt'
spider.craw(rootUrl, header, fileName)
