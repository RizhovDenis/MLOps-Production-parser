from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings
from crawler import settings
from crawler.spiders.company import CompanySpider


if __name__ == "__main__":
    crawler_settings = Settings()
    crawler_settings.setmodule(settings)
    crawler_proccess = CrawlerProcess(settings=crawler_settings)
    crawler_proccess.crawl(CompanySpider)
    crawler_proccess.start()

