import unittest

from src.checkout import Checkout
from src.model import Stock, Item

STORE_ITEMS = [
    Stock("A", 50),
    Stock("B", 30),
    Stock("C", 20),
    Stock("D", 15),
]


class CheckoutTest(unittest.TestCase):
    def setUp(self) -> None:
        # Lets create a few items
        self.item_a = Item(SKU="A")
        self.item_b = Item(SKU="B")
        self.item_c = Item(SKU="C")
        self.item_d = Item(SKU="D")
        self.customer_c = [self.item_a, self.item_b, self.item_b, self.item_b]

        self.checkout = Checkout()
        self.checkout.create_lookup(STORE_ITEMS)

    def test_basic_subtotal(self):
        result = self.checkout.basic_sub_total(self.customer_c)
        self.assertEqual(140, result)

    def tearDown(self) -> None:
        pass


if __name__ == "__main__":
    unittest.main()
