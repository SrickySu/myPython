#coding=utf-8
'''
Created on 2019年1月20日

@author: 74518
'''
import re
import urlparse
from bs4 import BeautifulSoup

class UrlParser(object):
    initTryTime = 3
    page = 0
    tryTime = initTryTime
    
    def __init__(self):
        self.page = 1
    
    def parse(self, url, content):
        if url is None or content is None:
            return
        soup = BeautifulSoup(content, 'html5lib', from_encoding='GBK')
        newUrl = self._getNewUrl(url, soup)
        newData = self._getData(soup)
        self.page += 1
        return newUrl, newData
    
    def _getNewUrl(self, url, soup):
        pageDiv = soup.find('div', targetid='table1')
        if pageDiv is None:
            if self.tryTime > 0:
                self.tryTime -= 1
                return url
            
            print 'page is none.'
            return
        if self.tryTime != self.initTryTime:
            self.tryTime = self.initTryTime
        
        nextPage = pageDiv.find('a', text='下一页')
        if nextPage is not None:
            pageIndex = self.page + 1
            if self.page == 1:
                backUrl = 'board/getHgtPage/page/' + pageIndex.__str__() + '/ajax/1/'
                return urlparse.urljoin(url, backUrl)
            match = re.findall(r'/\d+/', url)
            replacement = '/' + pageIndex.__str__() + '/'
            return url.replace(match[0], replacement)
        return
    
    def _getData(self, soup):
        table1 = soup.find('div', id='table1')
        if table1 is None:
            print 'table1 is none.'
            return
        newData = []
        if self.page == 1:
            ths = table1.find('thead').find_all('th')
            data = {}
            data[0] = ths[0].text
            data[1] = ths[1].text
            newData.append(data)
            return newData
        
        trTags = table1.find('tbody').find_all('tr')
        for tr in trTags:
            data = {}
            data[0] = tr.find_all('td')[0].text
            data[1] = tr.find_all('td')[1].text
            newData.append(data)
        return newData
    



