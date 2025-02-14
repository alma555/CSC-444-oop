from Catalog import Catalog
from Purchase import Purchase
from Item import Item

class ShoppingCart:
    def __init__(self, purchase_order: dict, catalog: Catalog):
        self.catalog = catalog

        purchase_order = list(purchase_order.items())
        purchases = []
        for purchase in purchase_order:
            purchases.append(Purchase(catalog.get_catalog()[purchase[0]],purchase[1]))
            #new purchase object
                #new item
                #quantity being purchased
        self.verify_shopping_cart(purchases)
        self.purchases = purchases

    def verify_shopping_cart(self, purchases: list):
        for purchase in purchases:
            if purchase.quantity < 0:
                raise ValueError("Shopping cart contains an order with an illegal quantity")
        
    def get_shopping_cart_total(self):
        total = 0
        for purchase in self.purchases:
            total += purchase.get_price()
        return total

    def get_shopping_cart_quantity(self):
        total = 0
        for purchase in self.purchases:
            total += purchase.get_quantity()
        return total

        
