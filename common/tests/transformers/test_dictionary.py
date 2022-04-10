from unittest import TestCase


from common.enums import NamingConventions
from common.transformers.dictionary import TransformDictionary

class TestTransformDictionary(TestCase):

    def test_update_naming_conventions_from_snake_to_camel(self):
        mocked_dictionary = {
            "param": "",
            "_snake_param": "",
            "__snake_param2": ""
        }

        expected_dictionary = {
            "param": "",
            "snakeParam": "",
            "snakeParam2": ""
        }

        result = TransformDictionary.update_naming_convention(mocked_dictionary, NamingConventions.SNAKE, NamingConventions.CAMEL)

        self.assertEqual(expected_dictionary, result)
