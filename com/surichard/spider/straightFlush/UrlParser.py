#coding=utf-8
'''
Created on 2019年1月20日

@author: 74518
'''
import re
import urlparse
from bs4 import BeautifulSoup

class UrlParser(object):
    
    def parse(self, url, content):
        if url is None or content is None:
            return
        soup = BeautifulSoup(content, 'html.parser', from_encoding='gbk')
        newUrl = self._getNewUrl(url, soup)
        newData = self._getData(url, soup)
        return newUrl, newData
    
    def _getNewUrl(self, url, soup):
        newUrls = set()
        links = soup.find_all('a', href=re.compile(r"/item/.*/\d+"))
        print 'length of links is', len(links)
        for link in links:
            newUrl = link['href']
            newUrls.add(urlparse.urljoin(url, newUrl))
        return newUrls
    
    def _getData(self, url, soup):
        newData = {}
        newData['url'] = url
        newData['title'] = soup.find('dd', class_="lemmaWgt-lemmaTitle-title").find('h1').get_text()
        newData['summary'] = soup.find('div', class_="lemma-summary").find('div').get_text()
        return newData
    



