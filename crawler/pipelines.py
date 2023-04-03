# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from database.db_sync import db_session
from components.company.models import Company
from components.news.models import News

class CrawlerPipeline:

    def process_item(self, item, spider):
        if item['name']:
            Company.insert(
                name=item['name'],
                description=item['description'],
                news_url=item['news_url']
            )
        else:
            News.insert(
                title=item['title'],
                content=item['content'],
                created_at=item['created_at'],
                company_id=item['company_id']
            )

        return item
