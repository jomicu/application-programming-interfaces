def is_variable_an_object(variable):
    return hasattr(variable, "__dict__")


def is_variable_an_dictionary(variable):
    return type(variable) is dict


def get_variable_type(variable):
    return type(variable).__name__

