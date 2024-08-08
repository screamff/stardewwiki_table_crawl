import scrapy
from stardewwiki.items import FishItem

class FishSpider(scrapy.Spider):
    name = 'fish'
    start_urls = [r'https://zh.stardewvalleywiki.com/鱼']

    def parse(self, response):
        table = response.css('table.wikitable')[0]
        tr_list = table.css('table.wikitable>tbody>tr')[1:]
        for tr in tr_list:
            图片 = tr.xpath('./td')[0].css('img').attrib.get('src')
            名称 = tr.xpath('./td')[1].css('a::text').get()
            描述 = tr.xpath('./td')[2].css('::text').get().strip()
            基础价格 = '/'.join([i.strip() for i in tr.xpath('./td')[3].css('tr').css('td::text').getall()])
            渔夫价格 = '/'.join([i.strip() for i in tr.xpath('./td')[4].css('tr').css('td::text').getall()])
            垂钓者价格 = '/'.join([i.strip() for i in tr.xpath('./td')[5].css('tr').css('td::text').getall()])
            位置 = '/'.join([i.strip() for i in tr.xpath('./td')[6].css('::text').getall()])
            时间 = '/'.join([i.strip() for i in tr.xpath('./td')[7].css('::text').getall()])
            季节 = '/'.join([i.strip() for i in tr.xpath('./td')[8].css('a::text').getall()])
            天气 = '/'.join([i.strip() for i in tr.xpath('./td')[9].css('a::text').getall()])
            尺寸 = tr.xpath('./td')[10].css('::text').get().strip()
            难度和行为 = tr.xpath('./td')[11].css('::text').get().strip()
            基础经验 = tr.xpath('./td')[12].css('::text').get().strip()
            用途 = '/'.join([i.strip() for i in tr.xpath('./td')[13].css('a::text').getall()])
            yield FishItem(图片=图片,
                           名称=名称,
                           描述=描述,
                           基础价格=基础价格,
                           渔夫价格=渔夫价格,
                           垂钓者价格=垂钓者价格,
                           位置=位置,
                           时间=时间,
                           季节=季节,
                           天气=天气,
                           尺寸=尺寸,
                           难度和行为=难度和行为,
                           基础经验=基础经验,
                           用途=用途)
