from dataclasses import dataclass, field
from time import time

@dataclass(frozen=True)
class Product(object):

    id: str
    name: str
    type: str
    unit: str
    creation_timestamp: int = field(default=round(time()))
    pictures: list[str] = field(default_factory=list)
    brand: str = field(default="Unknown")
    description: str = field(default=None)
    tags: list[str] = field(default_factory=list)
