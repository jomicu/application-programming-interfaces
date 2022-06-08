from dataclasses import dataclass, field

from common.decorators import custom_dataclass

@custom_dataclass
@dataclass(frozen=True)
class Product(object):

    id: str
    name: str
    type: str
    unit: str
    description: str = field(default=None)
    tags: list[str] = field(default_factory=list)
