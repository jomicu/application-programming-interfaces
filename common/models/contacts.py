from dataclasses import dataclass, field

@dataclass(frozen=True)
class Contacts(object):

    telephone: str = field(default=None)
    email: str = field(default=None)
