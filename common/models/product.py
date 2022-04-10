from pydantic import validate_arguments
from dataclasses import dataclass


@validate_arguments
@dataclass(frozen=True)
class Product(object):

    id: str
    name: str
    description: str
    unit: str
    tags: list = []

