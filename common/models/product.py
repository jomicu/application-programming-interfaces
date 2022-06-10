from dataclasses import dataclass, field

@dataclass(frozen=True)
class Product(object):

    id: str
    name: str
    type: str
    unit: str
    pictures: list[str] = field(init=False, default_factory=list)
    brand: str = field(default="Unknown")
    description: str = field(default=None)
    tags: list[str] = field(default_factory=list)
