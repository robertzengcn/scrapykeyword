# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapysexkeywordItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    keyword = scrapy.Field()
    pass

# class EmailscrapyItem(scrapy.Item):
#     # define the fields for your item here like:
#     url = scrapy.Field()
#     email=scrapy.Field()
#     description=scrapy.Field()
#     pass
