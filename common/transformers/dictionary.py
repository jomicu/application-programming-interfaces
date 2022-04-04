from typing import Callable


from common.exceptions import InvalidParameterType, InvalidConfiguration
from common.utilities import is_variable_an_object, is_variable_an_dictionary
from common.enums import NamingConventions
from common.transformers.string import (
    parse_snake_to_camel,
    parse_snake_to_pascal,
    parse_camel_to_snake,
    parse_camel_to_pascal,
    parse_pascal_to_snake,
    parse_pascal_to_camel
)


class ObjectToDictionary(object):


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
        ignore_nones: bool = True, 
        properties_to_ignore: tuple = ()
    ) -> None:
        self._ignore_private_properties = ignore_private_properties
        self._ignore_nones = ignore_nones
        self._properties_to_ignore = properties_to_ignore


    def _get_items(self, variable):
        if is_variable_an_object(variable):
            return variable.__dict__.items()
        
        if is_variable_an_dictionary(variable):
            return variable.items()
        
        raise InvalidParameterType("")

    
    def _is_valid_key(self, key: str) -> bool:
        if self._ignore_private_properties and key.startswith("_"):
            return False

        if key in self._properties_to_ignore:
            return False

        return True

    
    def _format_key(self, key: str) -> str:
        if not self._ignore_private_properties:
            private_prefix = "_"
            if key.startswith(private_prefix):
                key = key.removeprefix(private_prefix)
        return key

    
    def parse(self, variable) -> dict:
        dictionary = dict()
        items = self._get_items(variable)

        for key, value in items:
            if self._is_valid_key(key):
                key = self._format_key(key)
                if is_variable_an_object(value) or is_variable_an_dictionary(value):
                    dictionary[key] = self.parse(value)
                elif value is None:
                    if not self._ignore_nones:
                        dictionary[key] = value
                else:
                    dictionary[key] = value
        return dictionary


class DictionaryTransformer(object):

    
    @staticmethod
    def _update_key_names(dictionary: dict, parser: Callable) -> dict:
        updated_dict = dict()
        for key, value in dictionary.items():
            new_key = parser(key)
            if is_variable_an_dictionary(value):
                updated_dict[new_key] = DictionaryTransformer._update_key_names(value, parser)
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

        return DictionaryTransformer._update_key_names(dictionary, parser)
    
