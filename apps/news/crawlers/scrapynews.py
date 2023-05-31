from itemadapter import ItemAdapter
import scrapy
from scrapy.crawler import CrawlerProcess


from django.core.exceptions import ObjectDoesNotExist

from ..models import News, Category


class ArticleItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    category = scrapy.Field()


class SpiderPipeline(object):
    articles = []

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        self.articles.append({
            "title": adapter['title'],
            "link": adapter['link'],
            "category": adapter['category'],
        })

        return item

    def close_spider(self, spider):
        for attr in self.articles:
            title = attr.get('title')
            link = attr.get('link')
            category = attr.get('category')
            News(title=title, link=link, category=Category(id=category)).save()


class PoliticalSpider(scrapy.Spider):
    name = 'radiosvoboda'
    allowed_domains = ['radiosvoboda.org']
    start_urls = ['https://www.radiosvoboda.org/z/2730']
    custom_settings = {
        'ITEM_PIPELINES': {
            SpiderPipeline: 300,
        }
    }

    def parse(self, response):

        try:
            cat = Category.objects.get(title='політика')
        except ObjectDoesNotExist:
            Category(title='політика').save()
            cat = Category.objects.get(title='політика')

        content = response.xpath("//div/ul/li/div/div")

        for article in content:
            title = article.xpath("a/h4/text()").get().replace('\n', '')
            link = 'radiosvoboda.org' + article.xpath("a/@href").get()
            date = article.xpath("span/text()").get()
            category = int(cat.id)

            if date is None:
                continue
            else:
                yield ArticleItem(title=title, link=link, category=category)


class EconomicSpider(scrapy.Spider):
    name = 'bbc_ukraine'
    allowed_domains = ['bbc.com']
    start_urls = ['https://www.bbc.com/ukrainian/topics/cpzd47779gvt']
    custom_settings = {
        'ITEM_PIPELINES': {
            SpiderPipeline: 300,
        }
    }

    def parse(self, response):

        try:
            cat = Category.objects.get(title='економіка')
        except ObjectDoesNotExist:
            Category(title='економіка').save()
            cat = Category.objects.get(title='економіка')

        content = response.xpath("//ul/li/div")

        for article in content:
            title = article.xpath("div/h2/a/text()").get()
            link = article.xpath("div/h2/a/@href").get()
            category = int(cat.id)

            yield ArticleItem(title=title, link=link, category=category)
