from datetime import datetime, timedelta

import scrapy

from crawler.items import CrawlerItem

from components.company.models import Company

from settings import proj_conf


class NewsSpider(scrapy.Spider):
    name = 'news'
    start_urls = ['https://ru.investing.com/equities/russia']

    def parse(self, response, **kwargs):
        companies = Company.get_all()

        for company in companies:
            yield response.follow(
                company.news_url,
                callback=self.parse_news_urls,
                cb_kwargs={
                    'company_id': company.id,
                    'news_url': company.news_url
                }
            )

    def parse_news_urls(self, response, **kwargs):
        page_num = response.css('div.midDiv a.pagination.selected::text').get()
        pages_nums = response.css('div.midDiv a.pagination::text').getall()

        if not pages_nums or not page_num:
            return

        page_num = int(page_num)
        last_page_num = int(pages_nums[-1])

        if page_num <= last_page_num:
            sections = response.css('section div.textDiv')
            posts_titles = sections.css('a.title::text').getall()
            list_created_at = sections.css('span.date::text').getall()
            posts_urls = sections.css('a.title::attr(href)').getall()

            yield response.follow(
                kwargs['news_url'] + f'/{page_num+1}',
                callback=self.parse_news_urls,
                cb_kwargs=kwargs
            )

            for post_url, post_title, created_at in zip(posts_urls, posts_titles, list_created_at):
                if created_at.count('час') == 1:
                    delta = timedelta(hours=int(created_at[3:].split(' ')[0]))
                    kwargs['created_at'] = datetime.now() + delta

                elif created_at.count('мин') == 1:
                    delta = timedelta(minutes=int(created_at[3:].split(' ')[0]))
                    kwargs['created_at'] = datetime.now() + delta

                else:
                    kwargs['created_at'] = datetime.strptime(created_at[3:], "%d.%m.%Y")

                kwargs['post_title'] = post_title
                kwargs['url'] = proj_conf.parsing_source + post_url

                yield response.follow(
                    post_url,
                    callback=self.parse_news,
                    cb_kwargs=kwargs
                )

    def parse_news(self, response, **kwargs):
        content = response.css('div.WYSIWYG.articlePage p::text').getall()
        if content:
            content = ' '.join(content)

        crawler_item = CrawlerItem()
        crawler_item['name'] = None
        crawler_item['description'] = None
        crawler_item['news_url'] = None

        crawler_item['post_title'] = kwargs['post_title']
        crawler_item['created_at'] = kwargs['created_at']
        crawler_item['content'] = content
        crawler_item['url'] = kwargs['url']

        crawler_item['company_id'] = kwargs['company_id']

        yield crawler_item
