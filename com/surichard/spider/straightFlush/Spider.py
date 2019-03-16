#coding=utf-8
'''
Created on 2019年1月20日

@author: 74518
'''
import UrlManager, Downloader, UrlParser, OutputManager

class Spider(object):
    def __init__(self):
        self.urlManager = UrlManager.UrlManager()
        self.downloader = Downloader.Downloader()
        self.urlParser = UrlParser.UrlParser()
        self.outputManager = OutputManager.OutputManager()
    
    def craw(self, rootUrl, fileName):
        startFlag = True
        self.urlManager.addUrl(rootUrl)
        while self.urlManager.hasUrl():
            url = self.urlManager.getUrl()
            #try:
            content = self.downloader.download(rootUrl, url, startFlag, self.urlParser)
            newUrl, data = self.urlParser.parse(url, content)
            self.urlManager.addUrl(newUrl)
            self.outputManager.collectData(data)
            startFlag = False
#             except:
#                 print 'craw failed'
            
        self.outputManager.output(fileName)

spider = Spider()
rootUrl = 'http://data.10jqka.com.cn/hgt/sgtb/'
fileName = u'深股通.txt'
spider.craw(rootUrl, fileName)
