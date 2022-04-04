from os import environ


from common.models.product import Product
from common.transformers.dictionary import ObjectToDictionary
from common.aws.dynamo import DynamoDB


class ProductsTable(DynamoDB):


    def __init__(self):
        super().__init__(environ.get("PRODUCTS_TABLE_NAME"), "Id", "")

    
    def create_product(self, product: Product):
        transformer = ObjectToDictionary()
        item = transformer.parse(product)
        self._create_item(item)


    def get_product_by_id(self, id: str):
        return