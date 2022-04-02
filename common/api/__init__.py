import json


from common.enums.naming_conventions import NamingConventions
from common.transformers.dictionary import DictionaryTransformer


def handle_request_body(body: str):
    body = json.loads(body)
    return DictionaryTransformer.update_naming_convention(body, NamingConventions.CAMEL, NamingConventions.SNAKE)


# TODO cors and headers
def handle_response(event: dict, status_code: int, body: dict = None):
    valid_cors_origins = ""
    headers = ""
    
    response = dict()
    response["statusCode"] = status_code

    if body is not None:
        body = DictionaryTransformer.update_naming_convention(body, NamingConventions.SNAKE, NamingConventions.CAMEL)
        response["body"] = json.dumps(body)

    return response