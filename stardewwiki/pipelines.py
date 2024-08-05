# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pathlib import Path
import json

current_folder = Path(__file__).resolve().parent
out_path = current_folder / 'temp'
out_path.mkdir(parents=True, exist_ok=True)

class StardewwikiPipeline:
    def open_spider(self, spider):
        self.items = []

    def close_spider(self, spider):
        with open(out_path / "results.json", "w", encoding='utf-8') as file:
            json.dump(self.items, file, ensure_ascii=False, indent=2)

    def process_item(self, item, spider):
        self.items.append(dict(item))
        return item
