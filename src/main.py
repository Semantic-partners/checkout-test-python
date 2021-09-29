#!/usr/bin/env python
from src.checkout import Checkout
from src.model import Item, Stock

STORE_ITEMS = [
    Stock("A", 50, True, 130, 3),
    Stock("B", 30, True, 45, 2),
    Stock("C", 20, False, None, None),
    Stock("D", 15, False, None, None),
]

if __name__ == "__main__":
    # Lets create a few items
    item_a = Item(SKU="A")
    item_b = Item(SKU="B")
    item_c = Item(SKU="C")
    item_d = Item(SKU="D")

    # Create some customers
    customer_a = [item_d, item_a]
    customer_b = [item_c, item_b, item_a]
    customer_c = [item_a, item_b, item_b, item_b]

    # Create a checkout
    checkout = Checkout(operative_name="Wood Mackenzie")
    checkout.create_lookup(STORE_ITEMS)
    print(f"Customer A subtotal: {checkout.basic_sub_total(customer_a)}")
    print(f"Customer B subtotal: {checkout.basic_sub_total(customer_b)}")
    print(f"Customer C subtotal: {checkout.basic_sub_total(customer_c)}")
