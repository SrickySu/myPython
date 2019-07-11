# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy.utils.project as project
import pymysql

class MyspiderPipeline(object):
    def __init__(self):
        self.settings = project.get_project_settings()
        self.conn = pymysql.connect(host = self.settings.get('MYSQL_HOST'),
                        port=self.settings.get('MYSQL_PORT'),
                        db=self.settings.get('MYSQL_DB'),
                        user=self.settings.get('MYSQL_USER'),
                        passwd=self.settings.get('MYSQL_PASSWORD'),
                        charset = 'utf8',
                        use_unicode = True)
        self.cursor = self.conn.cursor()
        self.conn.autocommit(True)

    def process_item(self, item, spider):
        record = dict(item)
        insert_sql = 'insert into douban_movie(movie_name, description, star)' \
                     'values(%(movieName)s, %(description)s, %(star)s)'
        self.cursor.execute(insert_sql, record)
        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()
