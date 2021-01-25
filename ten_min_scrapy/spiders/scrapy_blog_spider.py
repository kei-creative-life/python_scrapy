import scrapy
import pdb
from ten_min_scrapy.items import Post

class ScrapyBlogSpiderSpider(scrapy.Spider):
    name = 'scrapy_blog_spider'
    allowed_domains = ['spesperficio.com']
    start_urls = ['http://spesperficio.com']


    def parse(self, response):
        div_item_lists = response.css('div.post-tab__content')
        for div_item_list in div_item_lists:
            # pdb.set_trace()
            for div_item in div_item_list.css('article.cardtype__article'):

                # 記事URLの取得
                item_url = div_item.css('a.cardtype__link::attr(href)').extract_first()

                # 記事URLを個別にスクレイピング
                yield scrapy.Request(item_url, callback=self.parse_item_page)

    def parse_item_page(self, response):
        items = []

        # 記事URLの取得
        item_url = response.url.strip()

        # 記事見出しの取得
        item_name = response.css('h1.entry-title::text').extract_first()
        item_name = item_name.strip()

        # 解析した内容を辞書にする
        item_info = {
            'name': item_name,
            'url': item_url
        }

        items.append(item_info)

        return item_info
