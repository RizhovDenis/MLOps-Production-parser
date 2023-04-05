# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    description = scrapy.Field()
    news_url = scrapy.Field()

    post_title = scrapy.Field()
    created_at = scrapy.Field()
    content = scrapy.Field()
    url = scrapy.Field()

    company_id = scrapy.Field()
