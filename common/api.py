import json


from common.enums import NamingConventions
from common.transformers.dictionary import TransformDictionary


def handle_request_body(body: str):
    body = json.loads(body)
    return TransformDictionary.update_naming_convention(body, NamingConventions.CAMEL, NamingConventions.SNAKE)


# TODO cors and headers
def handle_response(event: dict, status_code: int, body: dict = None):
    valid_cors_origins = ""
    headers = ""
    
    response = dict()
    response["statusCode"] = status_code

    if body is not None:
        body = TransformDictionary.update_naming_convention(body, NamingConventions.SNAKE, NamingConventions.CAMEL)
        response["body"] = json.dumps(body)

    return response