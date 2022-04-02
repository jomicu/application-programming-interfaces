from decimal import Decimal


def is_variable_an_object(variable):
    return hasattr(variable, "__dict__")


def is_variable_an_dictionary(variable):
    return type(variable) is dict


def to_dictionary(
        variable,
        ignore_nones = False,
        keys_to_ignore=[]
    ):
    dictionary = dict()

    if is_variable_an_object(variable):
        items = variable.__dict__.items()
    elif is_variable_an_dictionary(variable):
        items = variable.items()
    else:
        raise Exception()

    for key, value in items:
        if key not in keys_to_ignore:
            if is_variable_an_object(value) or is_variable_an_dictionary(value):
                to_dictionary(value)
            elif value is None:
                if not ignore_nones:
                    dictionary[key] = value
            else:
                dictionary[key] = value

    return dictionary



def object_to_dictionary(obj, parse_decimal_to_float=False, ignore_decimals=False, ignore_nones=False):
    mapped_dict = {}

    for property, value in obj.__dict__.items():
        if is_variable_an_object(value):
            mapped_dict[property] = object_to_dict(value, parse_decimal_to_float, ignore_decimals, ignore_nones)

        elif isinstance(value, Decimal):
            if not ignore_decimals:
                if parse_decimal_to_float:
                    mapped_dict[property] = float(value)
                else:
                    mapped_dict[property] = value
        
        elif value is None:
            print("yes")
            print(property)
            if not ignore_nones:
                mapped_dict[property] = value

        else:
            mapped_dict[property] = value

    return mapped_dict