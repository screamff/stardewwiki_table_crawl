import scrapy

class BundleSpider(scrapy.Spider):
    name = 'bundle'
    start_urls = [r'https://zh.stardewvalleywiki.com/收集包']

    def parse(self, response):
        tables = response.css('table.wikitable')
        is_crawling_room_name = True
        is_jinku = False
        item = {}
        for table in tables[:-2]:
            is_crawling_room_name = table.attrib.get('style')
            if is_crawling_room_name:
                if item:
                    yield item
                item = {}
                收集包房间 = table.css('th::text')[1].get()

                if 收集包房间 == '金库':
                    is_jinku = True
                    continue
                else:
                    is_jinku =False

                item['收集包房间']=收集包房间
                item['收集包'] = []
                continue
            elif not is_jinku:
                bundle_item = {}
                rows = table.xpath('./tbody/tr')
                收集包名称 = rows[0].css('th::text').get().strip()
                所需数量 = len(rows[1].xpath('./td')[1].xpath('./div'))

                bundle_item['收集包名称'] = 收集包名称
                bundle_item['所需数量'] = 所需数量
                bundle_item['物品'] = []

                物品名称 = ''.join(rows[1].xpath('./td')[2].css('::text').getall()[1:]).strip()
                物品链接 = response.urljoin(rows[1].xpath('./td')[2].css('a').attrib.get('href'))
                物品图片链接 = rows[1].xpath('./td')[2].css('img').attrib.get('src')
                # bundle_item['物品'].append({'物品名称':物品名称})
                bundle_item['物品'].append({'物品名称':物品名称, '物品链接':物品链接, '物品图片链接':物品图片链接})

                for row in rows[2:-1]:
                    物品名称 = ''.join(row.xpath('./td')[0].css('::text').getall()).strip()
                    物品链接 = response.urljoin(row.xpath('./td')[0].css('a').attrib.get('href'))
                    物品图片链接 = row.xpath('./td')[0].css('img').attrib.get('src')
                    # bundle_item['物品'].append({'物品名称':物品名称})
                    bundle_item['物品'].append({'物品名称':物品名称, '物品链接':物品链接, '物品图片链接':物品图片链接})

                item['收集包'].append(bundle_item)

        yield self.parse_last_table(response, tables[-1])

    def parse_last_table(self, response, last_table):
        item = {}
        item['收集包房间']='废弃Joja超市'
        item['收集包'] = []
        bundle_item = {}
        rows = last_table.xpath('./tbody/tr')
        收集包名称 = rows[0].css('th::text').get().strip()
        所需数量 = len(rows[1].xpath('./td')[1].xpath('./div'))
        bundle_item['收集包名称'] = 收集包名称
        bundle_item['所需数量'] = 所需数量
        bundle_item['物品'] = []
        for row in rows[2:-1]:
            物品名称 = ''.join(row.xpath('./td')[0].css('::text').getall()).strip()
            物品链接 = response.urljoin(row.xpath('./td')[0].css('a').attrib.get('href'))
            物品图片链接 = row.xpath('./td')[0].css('img').attrib.get('src')
            # bundle_item['物品'].append({'物品名称':物品名称})
            bundle_item['物品'].append({'物品名称':物品名称, '物品链接':物品链接, '物品图片链接':物品图片链接})

        item['收集包'].append(bundle_item)
        return item
