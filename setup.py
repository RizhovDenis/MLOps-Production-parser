from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings
from crawler import settings
from crawler.spiders.company import CompanySpider
from crawler.spiders.news import NewsSpider


if __name__ == "__main__":
    crawler_settings = Settings()
    crawler_settings.setmodule(settings)
    crawler_proccess = CrawlerProcess(settings=crawler_settings)
    crawler_proccess.crawl(CompanySpider)
    crawler_proccess.start()
    crawler_proccess.stop()
    print('therer')
    crawler_proccess.crawl(NewsSpider)
    crawler_proccess.start()

