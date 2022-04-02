import re


def is_variable_an_object(variable):
    return hasattr(variable, "__dict__")


def is_variable_an_dictionary(variable):
    return type(variable) is dict


def get_variable_type(variable):
    return type(variable).__name__


def parse_snake_to_camel(snake_str: str):
    components = snake_str.lstrip("_").split("_")
    return components[0] + "".join(x.title() for x in components[1:])


def parse_camel_to_snake(camel_str: str):
    camel_str = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', camel_str)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', camel_str).lower()