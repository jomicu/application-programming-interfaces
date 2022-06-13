from dataclasses import dataclass, field, asdict

from common.utilities import asdict_without_nones
from common.api import handle_request, handle_response
from common.models.product import Product
from products_table import ProductsTable

@dataclass(frozen=True)
class RequestQueryParameters(object):

    id: str = field(default=None)
    name: str = field(default=None)
    brand: str = field(default=None)

@dataclass(frozen=True)
class ResponseBody(Product):

    products: list[Product] = field(default=None)

def handler(event, context):
    request = handle_request(event)
    queryStringParameters = request["queryStringParameters"]

    if len(queryStringParameters) != 1:
        raise ValueError("Expected exactly 1 query string parameter but less or more were given.")

    products_table = ProductsTable()
    products: list[Product] = products_table.get(**queryStringParameters)

    if len(products) == 0:
        # TODO
        return handle_response(event, 404)

    print(products)

    return handle_response(event, 200, asdict_without_nones(ResponseBody(products)))
