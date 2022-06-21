from dataclasses import dataclass, asdict
from uuid import uuid4

from common.models.product import Product
from lib.products_database import ProductsTable

@dataclass(frozen=True)
class Request(object):

    products: list[dict]

@dataclass(frozen=True)
class Response(object):

    status_code: int
    products: list[Product]    

def handler(event, context):
    request = Request(**event)

    products = [Product(id=str(uuid4()), **product) for product in request.products]

    products_table = ProductsTable()
    products_table.save(products)

    return asdict(Response(201, products))
