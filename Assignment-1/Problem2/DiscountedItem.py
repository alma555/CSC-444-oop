from Item import Item

class DiscountedItem(Item):
    def __init__(self, name: str, price: float, bulk_quantity: int, bulk_price: float):
        self.name = name
        self.price = price
        self.bulk_quantity = bulk_quantity
        self.bulk_price = bulk_price
    
    def price_for(self, quantity: int):
        if quantity < self.bulk_quantity:
            return self.price * quantity
        if quantity >= self.bulk_quantity:
            normal_price_quantity = quantity % self.bulk_quantity
            discounted_quantity = quantity - normal_price_quantity
            total_cost = discounted_quantity * self.bulk_price
            total_cost += normal_price_quantity * self.price
            return total_cost

