from common.models.contacts import Contacts
from common.models.address import Address

class User(object):

    def __init__(
        self, 
        first_name: str, 
        last_name: str, 
        age: int, 
        contacts: dict, 
        address: dict
    ) -> None:
        self._first_name = first_name
        self._last_name = last_name
        self._age = age
        self._contacts = Contacts(**contacts)
        self._address = Address(**address)


    @property
    def first_name(self):
        return self._first_name

    
    @property
    def last_name(self):
        return self._last_name

    
    @property
    def age(self):
        return self._age

    @property
    def contacts(self):
        return self._contacts


    @property
    def address(self):
        return self._address