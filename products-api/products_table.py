from os import environ


from common.models.product import Product
from common.transformers.dictionary import TransformToDictionary
from common.aws.dynamo import DynamoDB


class ProductsTable(DynamoDB):


    def __init__(self):
        super().__init__(environ.get("PRODUCTS_TABLE_NAME"), "Name", "Id")


    def get_product_by_id(self, id: str):
        return self._get_item_by_sort_key(id)


    def get_product_by_name(self, name: str):
        item = self._get_item_by_hash_key(name)
        return Product(**item)

    
    def get_product_by_id_and_name(self, id: str, name: str)


    
    def save_product(self, product: Product):
        transformer = TransformToDictionary()
        item = transformer.parse(product)
        self._create_item(item)

