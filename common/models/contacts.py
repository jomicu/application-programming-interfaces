class Contacts(object):


    def __init__(self, telephone=None, email=None):
        self._telephone = telephone
        self._email = email


    @property
    def telephone(self):
        return self._telephone

    
    @property
    def email(self):
        return self._email

        