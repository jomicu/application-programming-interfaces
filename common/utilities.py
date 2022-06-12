from dataclasses import asdict

def is_variable_an_object(variable):
    return hasattr(variable, "__dict__")


def is_variable_an_dictionary(variable):
    return type(variable) is dict


def is_variable_a_list(variable):
    return type(variable) is list


def get_variable_type(variable):
    return type(variable).__name__

def asdict_without_nones(dataclass):
    asdict(dataclass, dict_factory=lambda x: {k: v for (k, v) in x if v is not None})

