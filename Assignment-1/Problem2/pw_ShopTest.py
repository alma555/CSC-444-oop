from ShoppingCart import ShoppingCart
from Purchase import Purchase
from Catalog import Catalog
from DiscountedItem import DiscountedItem
from Item import Item

def parse_items_from_file(file_path, store_name):
    catalog = Catalog(store_name)
    with open(file_path, 'r') as file: 
        for line in file:
            if not line.strip():  # Skip empty lines
                continue
            parts = line.split(',')
            name = parts[0].strip()
            price = float(parts[1].strip())

            if len(parts) == 2:  # Only name and price
                catalog.add(Item(name, price))
            elif len(parts) == 4:  # Name, price, bulk quantity, and bulk price
                bulk_quantity = int(parts[2].strip())
                bulk_price = float(parts[3].strip())
                catalog.add(DiscountedItem(name, price, bulk_quantity, bulk_price))
    return catalog

if __name__ == '__main__':
    catalog = parse_items_from_file('pw_catalog.txt', 'Prof. Wu\'s Store')

    try:
        purchase_order = {'LEGO Race Car': 10, 'Egg': 15, 'USB-C Cord': 2, 'Turtles': 3}
        sc = ShoppingCart(purchase_order, catalog)
    except Exception as e:
        print("Error correctly caught.")

    purchase_order = {'LEGO Race Car': 10, 'Egg': 15, 'USB-C Cord': 2, 'Desk Clock': 35}
    sc = ShoppingCart(purchase_order, catalog)
    print('Total: ' + str(sc.get_shopping_cart_total()))
