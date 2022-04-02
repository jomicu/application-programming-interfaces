class Address(object):


    def __init__(self, postcode=None):
        self._postcode = postcode

    
    @property
    def postcode(self):
        return self._postcode

