# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FishItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    图片 = scrapy.Field()
    名称 = scrapy.Field()
    描述 = scrapy.Field()
    基础价格 = scrapy.Field()
    渔夫价格 = scrapy.Field()
    垂钓者价格 = scrapy.Field()
    位置 = scrapy.Field()
    时间 = scrapy.Field()
    季节 = scrapy.Field()
    天气 = scrapy.Field()
    尺寸 = scrapy.Field()
    难度和行为 = scrapy.Field()
    基础经验 = scrapy.Field()
    用途 = scrapy.Field()
