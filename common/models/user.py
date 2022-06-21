from dataclasses import dataclass, field

from common.utilities import is_variable_an_dictionary
from common.models.contacts import Contacts
from common.models.address import Address

@dataclass(frozen=True)
class User(object):

    first_name: str
    last_name: str
    age: int
    contacts: Contacts = field(default=None)
    address: Address = field(default=None)

    def __post_init__(self):
        object.__setattr__(self, "contacts", Contacts(**self.contacts) if is_variable_an_dictionary(self.contacts) else self.contacts)
        object.__setattr__(self, "address", Address(**self.address) if is_variable_an_dictionary(self.address) else self.address)
