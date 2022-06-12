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
            logger.info(f"Searching for product with id: {id}")
            items = self._query(sort_key=id)
        elif name is not None:
            logger.info(f"Searching for products with name: {name}")
            items = self._query(hash_key=name)
        elif brand is not None:
            logger.info(f"Searching for products from the brand: {brand}")
            # TODO
        else:
            raise ValueError("Provided property values are not valid. All of them were defined as None.")

        products = [Product(**item) for item in items]
        logger.info(f"Products found: {products}")
        return products

    def update(self):
        pass

    def delete(self):
        pass
