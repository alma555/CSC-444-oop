class Item:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def get_name(self):
        return self.name

    def price_for(self, quantity: int):
        return self.price * quantity
