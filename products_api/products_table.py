from os import environ
from logging import INFO, getLogger
from dataclasses import asdict

from common.models.product import Product
from common.aws.dynamo import DynamoDB

logger = getLogger()
logger.setLevel(INFO)

class ProductsTable(DynamoDB):

    def __init__(self):
        super().__init__(environ.get("PRODUCTS_TABLE_NAME"), "Name", "Id")

    def get_product_by_id(self, id: str):
        return self._get_item_by_sort_key(id)

    def get_product_by_name(self, name: str):
        item = self._get_item_by_hash_key(name)
        return Product(**item)

    def save_product(self, product: Product):
        logger.info(f"Saving the following product {product} to Products table ...")
        self._create_item(asdict(product))
        logger.info(f"Finished saving product with id {product.id}!")

    def save_products(self, products: list[Product]):
        if len(products) == 1:
            self.save_product(products[0])
        else:
            logger.info(f"Saving the following products {products} to Products table ...")
            self._create_items([asdict(product) for product in products])
            logger.info("Finished saving products!")
