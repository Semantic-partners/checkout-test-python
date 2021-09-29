from collections import namedtuple

Item = namedtuple("StoreItem", ["SKU"])
Stock = namedtuple(
    "Catalogue", ["SKU", "UnitPrice"]
)
