from dataclasses import dataclass, asdict
from uuid import uuid4

from common.api import handle_request, handle_response
from common.models.product import Product
from products_table import ProductsTable

@dataclass(frozen=True)
class RequestBody(object):

    products: list[dict]

@dataclass(frozen=True)
class ResponseBody(object):

    products: list[Product]    

def handler(event, context):
    request = handle_request(event)
    request_body = RequestBody(**request["body"])

    products = [Product(id=str(uuid4()), **product) for product in request_body.products]

    products_table = ProductsTable()
    products_table.save(products)

    return handle_response(event, 201, asdict(ResponseBody(products)))
