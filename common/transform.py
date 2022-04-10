from typing import Callable
import re


from common.exceptions import InvalidParameterType, InvalidConfiguration
from common.utilities import is_variable_an_object, is_variable_an_dictionary, is_variable_a_list
from common.enums import NamingConventions


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

class TransformToDictionary(object):

    @staticmethod
    def _get_items(variable):
        if is_variable_an_object(variable):
            return variable.__dict__.items()
        
        if is_variable_an_dictionary(variable):
            return variable.items()
        
        raise InvalidParameterType("")


    """
    Possible values for the configuration:

        - ignore_private_properties: If set to true, any property that starts with
                                     "_" will be ignored. Default is false.

        - ignore_nones: Flag that says if we should filter out any vale from being
                        added to the dictionary, result of the mapping, in case 
                        it's value is null (None). Default is true.

        - properties_to_ignore: Tuple that will contain the name of the properties that 
                                should be not added to the dictionary result of the
                                mapping. Default is an empty tuple.
    """
    def __init__(
        self, 
        ignore_private_properties: bool = False, 
        ignore_none_values: bool = True, 
        properties_to_ignore: tuple = ()
    ) -> None:
        self._ignore_private_properties = ignore_private_properties
        self._ignore_none_values = ignore_none_values
        self._properties_to_ignore = properties_to_ignore

    
    def _is_valid_property(self, property: str) -> bool:
        if self._ignore_private_properties and property.startswith("_"):
            return False
        if not property in self._properties_to_ignore:
            return False
        return True

    
    def _is_valid_value(self, value: any) -> bool:
        if self._ignore_none_values and value is None:
            return False
        return True

    
    def _format_property_name(self, property: str) -> str:
        if not self._ignore_private_properties:
            private_prefix = "_"
            if property.startswith(private_prefix):
                property = property.removeprefix(private_prefix)
        return property


    def _retrieve_new_value(self, value):
        if is_variable_an_object(value) or is_variable_an_dictionary(value):
            return self.parse(value)

        if is_variable_a_list(value):
            return self.parse_list_items_to_dictionary(value)

        return value


    def parse_list_items_to_dictionary(self, variable: list) -> list:
        result = list()
        for value in variable:
            if self._is_valid_value(value):
                result.append(self._retrieve_new_value(value))
        return result

 
    def parse_object_to_dictionary(self, variable) -> dict:
        dictionary = dict()
        items = TransformToDictionary._get_items(variable)
        for property, value in items:
            if self._is_valid_property(property) and self._is_valid_value(value):
                property = self._format_property_name(property)
                dictionary[property] = self._retrieve_new_value(value)
        return dictionary


class TransformDictionary(object):


    @staticmethod
    def _update_key_names(dictionary: dict, parser: Callable) -> dict:
        updated_dict = dict()
        for key, value in dictionary.items():
            new_key = parser(key)
            if is_variable_an_dictionary(value):
                updated_dict[new_key] = TransformDictionary._update_key_names(value, parser)
            else:
                updated_dict[new_key] = value
        return updated_dict


    """
    This function will iterate over the given dictionary keys and will update them accordingly
    to the given new name convention.

    Parameters:

        - dictionary: dictionary that will be iterated
    
        - current: current name convention in place for the given dictionary keys
    
        - new: new name convention to be applied to the given dictionary keys
    """
    @staticmethod
    def update_naming_convention(dictionary: dict, current: str, new: str) -> dict:

        if not isinstance(current, NamingConventions) or not isinstance(new, NamingConventions):
            raise InvalidParameterType()

        if current == new:
            raise InvalidConfiguration()

        parser = None

        if current == NamingConventions.SNAKE:
            if new == NamingConventions.CAMEL:
                parser = parse_snake_to_camel
            elif new == NamingConventions.PASCAL:
                parser = parse_snake_to_pascal
        elif current == NamingConventions.CAMEL:
            if new == NamingConventions.SNAKE:
                parser = parse_camel_to_snake
            elif new == NamingConventions.PASCAL:
                parser = parse_camel_to_pascal
        elif current == NamingConventions.PASCAL:
            if new == NamingConventions.SNAKE:
                parser = parse_pascal_to_snake
            elif new == NamingConventions.CAMEL:
                parser = parse_pascal_to_camel

        if parser is None:
            raise InvalidParameterType()

        return TransformDictionary._update_key_names(dictionary, parser)
    
