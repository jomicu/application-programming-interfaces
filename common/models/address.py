from dataclasses import dataclass, field

@dataclass(frozen=True)
class Address(object):

    postcode: str = field(default=None)
