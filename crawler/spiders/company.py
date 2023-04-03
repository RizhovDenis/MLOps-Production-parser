import time

import scrapy

from crawler.items import CrawlerItem


class ParseConfig:

    parsing_source: str = 'https://ru.investing.com'


class CompanySpider(scrapy.Spider):
    name = 'companies'
    start_urls = ['https://ru.investing.com/equities/russia']
    table_styles = 'datatable_table__D_jso.dynamic-table_dynamic-table__LN2WJ.datatable_table--mobile-basic__W2ilt.datatable_table--freeze-column__7YoIE.datatable_table--dynamic-table__l368m'

    def parse(self, response, **kwargs):
        table = response.css(f'table.{self.table_styles}')
        marks = table.css('a.inv-link.bold.datatable_cell--name__link__tmnQz')
        names = table.css('span.pt-2.font-normal.dynamic-table_cell-symbol__ORxgq::text')
        urls = marks.css('::attr(href)')

        for name, url in zip(names, urls):
            cur_url = ParseConfig.parsing_source + url.get()
            yield response.follow(
                cur_url,
                callback=self.parse_description,
                cb_kwargs={
                    'name': name.get(),
                    'cur_url': cur_url.split('?')[0]
                }
            )

    def parse_description(self, response, **kwargs):
        time.sleep(1)
        description = response.css('div.bg-background-surface p.text-xs::text').get()

        crawler_item = CrawlerItem()
        crawler_item['name'] = kwargs['name']
        crawler_item['description'] = description
        crawler_item['news_url'] = kwargs['cur_url'] + '-news'

        crawler_item['post_title'] = None
        crawler_item['created_at'] = None
        crawler_item['content'] = None
        crawler_item['company_id'] = None

        yield crawler_item
