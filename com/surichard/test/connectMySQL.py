# coding=utf-8
'''
Created on 2019年1月1日

@author: 74518
'''
import re, mysql.connector
class Person(object):
    def __init__(self, name, gender, birth, job):
        self.name = name
        self.gender = gender
        self.birth = birth
        self.job = job

xiaoming = Person('Xiao Ming', 'Male', '1990-1-1', job='Student')

print xiaoming.name
print xiaoming.job

conn = mysql.connector.Connect(host='', port='3306', user='root', password='', database='mysql', charset='utf8')
cursor = conn.cursor()
cursor.execute('select * from user limit 2')
results = cursor.fetchall()
for re in results:
    print re
conn.close()


