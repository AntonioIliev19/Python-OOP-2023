class Shop:
    def __init__(self, name, items):
        self.name = name
        self.items = items

    def get_items_count(self):
        return len(self.items)


shop = Shop("My Shop", ["Apples", "Bananas", "Cucumbers"])
billa = Shop("billa", ["Bila", "Pleskavica"])
print(shop.get_items_count())
print(billa.get_items_count())
