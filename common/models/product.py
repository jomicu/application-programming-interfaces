from dataclasses import dataclass, field
from uuid import uuid4

from common.utilities import is_variable_an_dictionary

@dataclass(frozen=True)
class Product(object):

    id: str
    name: str
    type: str
    unit: str
    brand: str = field(default="Unknown")
    description: str = field(default=None)
    tags: list[str] = field(default_factory=list)

@dataclass(frozen=True)
class Products(object):

    products: list[Product]

    def __init__(self, products):
        self.products = [
            Product(id=str(uuid4()), **product) if is_variable_an_dictionary(product) else product 
            for product in products
        ]

