from dataclasses import dataclass, field

from common.utilities import is_variable_an_dictionary
from common.decorators import custom_dataclass
from common.models.contacts import Contacts
from common.models.address import Address

@custom_dataclass
@dataclass(frozen=False)
class User(object):

    first_name: str
    last_name: str
    age: int
    contacts: Contacts = field(default=None)
    address: Address = field(default=None)

    def __post_init__(self):
        self.contacts = Contacts(**self.contacts) if is_variable_an_dictionary(self.contacts) else self.contacts
        self.address = Address(**self.address) if is_variable_an_dictionary(self.address) else self.address
