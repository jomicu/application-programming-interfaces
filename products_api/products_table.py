from os import environ
from logging import INFO, getLogger
from dataclasses import asdict

from common.models.product import Product
from common.aws.dynamo_database import DynamoDatabase

logger = getLogger()
logger.setLevel(INFO)

class ProductsTable(DynamoDatabase):

    def __init__(self):
        super().__init__(environ.get("PRODUCTS_TABLE_NAME"), "Name", "Id")

    def save(self, products: list[Product]) -> None:
        if len(products) == 1:
            product = products[0]
            logger.info(f"Saving the following product {product} to Products table ...")
            self._put(item=asdict(product))
            logger.info(f"Finished saving product with id {product.id}!")
        else:
            logger.info(f"Saving the following products {products} to Products table ...")
            self._put(items=[asdict(product) for product in products])
            logger.info("Finished saving products!")

    def get(self, id: str = None, name: str = None, brand: str = None) -> list[Product]:
        if id is not None:
            return self._query(sort_key=id)

        if name is not None:
            return self._query(hash_key=name)

        if brand is not None:
            return 

        raise ValueError("Provided property values are not valid. All of them were defined as None.")

    def update(self):
        pass

    def delete(self):
        pass
