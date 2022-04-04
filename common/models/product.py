class Product(object):

    def __init__(self, id: str, name: str, description: str, unit: str, tags: list) -> None:
        self._id = id
        self._name = name
        self._description = description
        self._unit = unit
        self._tags = tags


    @property
    def id(self):
        return self._id

    
    @property
    def name(self):
        return self._name

    
    @property
    def description(self):
        return self._description

    @property
    def unit(self):
        return self._unit

    
    @property
    def tags(self):
        return self._tags

