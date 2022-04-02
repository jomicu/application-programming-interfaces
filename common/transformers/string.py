import re


def parse_snake_to_camel(snake_str: str):
    components = snake_str.lstrip("_").split("_")
    return components[0] + "".join(x.title() for x in components[1:])


def parse_snake_to_pascal(snake_str: str):
    return snake_str.replace("_", " ").title().replace(" ", "")


def parse_camel_to_snake(camel_str: str):
    camel_str = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', camel_str)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', camel_str).lower()


def parse_camel_to_pascal(camel_str: str):
    return camel_str[0].upper() + camel_str[1:]


def parse_pascal_to_snake(pascal_str: str):
    return parse_camel_to_snake(pascal_str)


def parse_pascal_to_camel(pascal_str: str):
    return pascal_str[0].lower() + pascal_str[1:]