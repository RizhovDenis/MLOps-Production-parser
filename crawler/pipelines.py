# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import os

from itemadapter import ItemAdapter


class CrawlerPipeline:

    def __init__(self):
        pass
        # self.con = db_session

    def process_item(self, item, spider):
        # Company.insert(item['name'])
        return item
