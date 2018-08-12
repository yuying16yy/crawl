# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PokemonCrawlItem(scrapy.Item):
    # define the fields for your item here like:
    Name = scrapy.Field()
    Number= scrapy.Field()
    text = scrapy.Field()

