from Item import Item

class Purchase:
    def __init__(self, item: Item, quantity: int):
        self.item = item
        self.quantity = quantity

    def get_price(self):
        return self.item.price * self.quantity

    def get_quantity(self):
        return self.quantity
