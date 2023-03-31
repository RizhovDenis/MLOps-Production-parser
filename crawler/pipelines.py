# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from database.db_sync import db_session
from components.company.models import Company


class CrawlerPipeline:

    def process_item(self, item, spider):
        Company.insert(item['name'], None)
        return item
