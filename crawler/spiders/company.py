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
            yield response.follow(
                ParseConfig.parsing_source + url.get(),
                callback=self.parse,
                cb_kwargs={'name': name.get()}
            )

    def parse_description(self, response, **kwargs):
        crawler_item = CrawlerItem()
        crawler_item['name'] = kwargs['name']
        description = response.css('p.company-profile_profile-description__YWJVr')
        crawler_item['description'] = description
        yield
