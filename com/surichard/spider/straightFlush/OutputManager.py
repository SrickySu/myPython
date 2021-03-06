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
        if isinstance(data, list):
            for item in data:
                self.data.append(item)
        else:
            self.data.append(data)

    
    def output(self, fileName):
        file = open(fileName, 'w')
        for item in self.data:
            file.write('%s,%s' % (item[0].encode('utf-8'),item[1].encode('utf-8')))
            file.write('\n')
        file.close()
