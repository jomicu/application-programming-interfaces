from uuid import uuid4

from common.enums import Units
from common.models.product import Product

class ProductsFactory(object):

    @staticmethod
    def create_product(name: str, description: str = None, unit: str = Units.UNIT.value, tags: list = []):
        return Product(str(uuid4()), name, description, unit, tags)