import click

from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings
from crawler import settings


@click.group(name='parser')
def group(): ...


@group.command(name='parse_companies')
def parse_companies():
    from crawler.spiders.company import CompanySpider

    crawler_settings = Settings()
    crawler_settings.setmodule(settings)
    crawler_proccess = CrawlerProcess(settings=crawler_settings)
    crawler_proccess.crawl(CompanySpider)
    crawler_proccess.start()


@group.command(name='parse_news')
def parse_news():
    from crawler.spiders.news import NewsSpider

    crawler_settings = Settings()
    crawler_settings.setmodule(settings)
    crawler_proccess = CrawlerProcess(settings=crawler_settings)
    crawler_proccess.crawl(NewsSpider)
    crawler_proccess.start()


if __name__ == "__main__":
    group()
