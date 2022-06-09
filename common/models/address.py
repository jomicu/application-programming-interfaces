from dataclasses import dataclass, field

from common.decorators import custom_dataclass

@custom_dataclass
@dataclass(frozen=True)
class Address(object):

    postcode: str = field(default=None)
