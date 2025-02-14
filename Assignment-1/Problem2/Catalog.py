from Item import Item

class Catalog:
    def __init__(self, store_name: str):
        self.store_name = store_name
        self.catalog = {}

    def add(self, item: Item):
        self.catalog.update({item.get_name() : item})

    def get_store_name(self):
        return self.store_name

    def get_catalog(self):
        return self.catalog
