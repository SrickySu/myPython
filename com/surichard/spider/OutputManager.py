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
        file = open('words.html', 'w')
        file.write('<html>')
        file.write('<body>')
        file.write('<table>')
        for item in self.data:
            file.write('<tr>')
            file.write('<td>%s</td>' % item['url'])
            file.write('<td>%s</td>' % item['title'].encode('utf-8'))
            file.write('<td>%s</td>' % item['summary'].encode('utf-8'))
            file.write('</tr>')
        file.write('</table>')
        file.write('</body>')
        file.write('</html>')
        file.close()
