from os import environ
from dataclasses import asdict

from models.product import Product
from dynamo_databases import DynamoDB

class ProductsTable(DynamoDB):

    def __init__(self):
        super().__init__(environ.get("PRODUCTS_TABLE_NAME"), "Name", "Id")

    def get_product_by_id(self, id: str):
        return self._get_item_by_sort_key(id)

    def get_product_by_name(self, name: str):
        item = self._get_item_by_hash_key(name)
        return Product(**item)

    def save_product(self, product: Product):
        self._create_item(asdict(product))
