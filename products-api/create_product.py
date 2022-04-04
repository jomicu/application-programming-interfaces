from common.api import handle_request_body, handle_response
from common.transformers.dictionary import ObjectToDictionary
from common.factories.products_factory import ProductsFactory
from common.models.product import Product
from products_table import ProductsTable


def handler(event, context):
    request_body: dict = handle_request_body(event["body"])

    products_factory = ProductsFactory()
    product: Product = products_factory.create_product(**request_body)

    products_table = ProductsTable()
    products_table.save_product(product)

    return handle_response(event, 201, build_response_body(product))


def build_response_body(product: Product):
    parser = ObjectToDictionary()
    return parser.parse(product)