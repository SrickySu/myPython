#coding=utf-8
'''
Created on 2019年1月20日

@author: 74518
'''
import re
import urlparse
from bs4 import BeautifulSoup

class UrlParser(object):
    page = 0;
    
    def parse(self, url, content):
        self.page = 1
        if url is None or content is None:
            return
        soup = BeautifulSoup(content, 'html5lib', from_encoding='GBK')
        newUrl = self._getNewUrl(url, soup)
        newData = self._getData(soup)
        return newUrl, newData
    
    def _getNewUrl(self, url, soup):
        nextPage = soup.find('div', targetid='table1').find('a', text='下一页')
        if nextPage is not None:
            self.page += 1
            backUrl = 'board/getHgtPage/page/' + self.page.__str__() + '/ajax/1/'
            return urlparse.urljoin(url, backUrl)
        return
    
    def _getData(self, soup):
        newData = []
        trTags = soup.find('div', id="table1").find('tbody').find_all('tr')
        for tr in trTags:
            data = {}
            data[0] = tr.find_all('td')[0].string
            data[1] = tr.find_all('td')[1].string
            newData.append(data)
        return newData
    



