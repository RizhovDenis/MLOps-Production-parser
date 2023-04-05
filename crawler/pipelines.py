# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from components.company.models import Company
from components.news.models import News
from components.companies_news.models import CompanyNews


class CrawlerPipeline:

    def process_item(self, item, spider):
        if item['name']:
            Company.insert(
                name=item['name'],
                description=item['description'],
                news_url=item['news_url']
            )
        elif item['content']:
            news = News.insert(
                title=item['post_title'],
                content=item['content'],
                created_at=item['created_at'],
                url=item['url']
            )

            CompanyNews.insert(
                company_id=item['company_id'],
                news_id=news.id
            )

        return item
