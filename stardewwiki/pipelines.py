# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from stardewwiki.items import FishItem
from pathlib import Path
import json

current_folder = Path(__file__).resolve().parent
out_path = current_folder / 'temp'
out_path.mkdir(parents=True, exist_ok=True)

class FishPipeline:
    def open_spider(self, spider):
        self.items = []

    def close_spider(self, spider):
        if self.items:
            with open(out_path / "results_fish.json", "w", encoding='utf-8') as file:
                json.dump(self.items, file, ensure_ascii=False, indent=2)

    def process_item(self, item, spider):
        if isinstance(item, FishItem):
            self.items.append(dict(item))
        return item


class BundlePipeline:
    def open_spider(self, spider):
        self.items = []

    def close_spider(self, spider):
        if self.items:
            with open(current_folder / "flask_show_data/results_bundle.json", "w", encoding='utf-8') as file:
                json.dump(self.items, file, ensure_ascii=False, indent=2)

    def process_item(self, item, spider):
        if not isinstance(item, FishItem):
            self.items.append(dict(item))
        return item
