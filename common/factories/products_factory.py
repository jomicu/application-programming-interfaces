from uuid import uuid4


from common.exceptions import InvalidParameterType
from common.enums import Units
from common.models.product import Product


class ProductsFactory(object):


    @staticmethod
    def create_product(name: str, description: str = None, unit: str = Units.UNIT.value, tags: list = []):

        id = uuid4()

        return Product(id, name, description, unit, tags)