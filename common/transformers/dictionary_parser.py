from common.exceptions.invalid_parameter import InvalidParameterType
from common.exceptions.invalid_configuration import InvalidConfiguration
from common.utilities import (
    is_variable_an_object, 
    is_variable_an_dictionary, 
    get_variable_type,
    parse_snake_to_camel,
    parse_camel_to_snake
)


class DictionaryParser(object):


    """
    Possible values for the configuration:

        - parse_to_snake_case: Flag that indicates if we want to parse the
                               dictionary or object properties name from
                               camel case to snake case. Default is false.

        - parse_to_camel_case: Flag that indicates if we want to parse the
                               dictionary or object properties name from
                               snake case to camel case. Default is false.

        - ignore_private_keys: Flag that says if during the mapping we should
                               or not ignore the private fields (anything 
                               that starts with "_" or "__" is considered to 
                               be a private field). Default is false.

        - parse_private_keys: In case the flah "ignore_private_keys" is set to
                              false, this attribute will define if we should
                              parse the private fields into normal dictionary
                              variables names (eg.: "_my_var" to "my_var" or
                              "__my_var" to "my_var")

        - ignore_nones: Flag that says if we should filter out any vale from being
                        added to the dictionary, result of the mapping, in case 
                        it's value is null (None). Default is true.

        - keys_to_ignore: Tuple that will contain the name of the properties that 
                          should be not added to the dictionary result of the
                          mapping. Default is an empty tuple.
    """
    def __init__(
        self,
        parse_to_snake_case: bool = False,
        parse_to_camel_case: bool = False,
        ignore_private_keys: bool = False,
        parse_private_keys: bool = True,
        ignore_nones: bool = True,
        keys_to_ignore: tuple = ()
    ) -> None:
        if parse_to_snake_case and parse_to_camel_case:
            raise InvalidConfiguration()

        if ignore_private_keys and parse_private_keys:
            raise InvalidConfiguration()

        self._parse_to_snake_case = parse_to_snake_case
        self._parse_to_camel_case = parse_to_camel_case
        self._ignore_private_keys = ignore_private_keys
        self._parse_private_keys = parse_private_keys
        self._ignore_nones = ignore_nones
        self._keys_to_ignore = keys_to_ignore


    def _is_valid_key(self, key: str) -> bool:
            if self._ignore_private_keys and key.startswith(("_", "__")):
                return False

            if key in self._keys_to_ignore:
                return False

            return True


    def _format_key(self, type, key: str) -> str:
        if self._parse_private_keys:
            more_private_prefix = f"_{type}__"
            private_prefix = "_"
            if key.startswith(more_private_prefix):
                key = key.removeprefix(more_private_prefix)
            elif key.startswith(private_prefix):
                key = key.removeprefix(private_prefix)

        if self._parse_to_snake_case:
            key = parse_camel_to_snake(key)
        elif self._parse_to_camel_case:
            key = parse_snake_to_camel(key)

        return key


    def _get_items(self, variable):
        if is_variable_an_object(variable):
            return variable.__dict__.items()
        
        if is_variable_an_dictionary(variable):
            return variable.items()
        
        raise InvalidParameterType("Not a valid type to parse to dictionary!")


    def parse(self, variable) -> dict:
        dictionary = dict()
        items = self._get_items(variable)

        for key, value in items:
            if self._is_valid_key(key):
                key = self._format_key(get_variable_type(variable), key)

                if is_variable_an_object(value) or is_variable_an_dictionary(value):
                    dictionary[key] = self.parse(value)
                
                elif value is None:
                    if not self._ignore_nones:
                        dictionary[key] = value
                
                else:
                    dictionary[key] = value

        return dictionary

