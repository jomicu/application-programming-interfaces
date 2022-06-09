from dataclasses import dataclass, field

from common.decorators import custom_dataclass

@custom_dataclass
@dataclass(frozen=True)
class Contacts(object):

    telephone: str = field(default=None)
    email: str = field(default=None)
