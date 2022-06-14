from dataclasses import dataclass, field

@dataclass(frozen=True)
class Product(object):

    id: str
    name: str
    type: str
    unit: str
    very_long_attribute: str = None
    pictures: list[str] = field(default_factory=list)
    brand: str = field(default="Unknown")
    description: str = field(default=None)
    tags: list[str] = field(default_factory=list)
