#coding=utf-8
'''
Created on 2019年1月20日

@author: 74518
'''


class OutputManager(object):
    def __init__(self):
        self.data = []
    
    def collectData(self, data):
        if data is None:
            return
        self.data.append(data)

    
    def output(self):
        file = open('data.txt', 'w')
        for item in self.data:
            file.write('%s,%s' % (item[0].encode('utf-8'), item[1].encode('utf-8')))
        file.close()
