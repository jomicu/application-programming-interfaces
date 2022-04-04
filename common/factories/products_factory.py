from uuid import uuid4


from common.exceptions import InvalidParameterType
from common.enums import Units
from common.models.product import Product


class ProductsFactory(object):


    def _get_product_id():
        return uuid4()


    def create_product(self, name: str, description: str = None, unit: str = Units.UNIT, tags: list = []):
        if not isinstance(unit, Units):
            raise InvalidParameterType()

        id = self._get_product_id()

        return Product(id, name, description, unit, tags)