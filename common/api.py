import json


from common.enums import NamingConventions
from common.transform import TransformDictionary


def handle_request_body(body: str):
    body = json.loads(body)
    return TransformDictionary.update_naming_convention(body, NamingConventions.CAMEL, NamingConventions.SNAKE)


# TODO cors and headers
def handle_response(event: dict, status_code: int, body: dict = None):
    valid_cors_origins = ""
    headers = ""
    
    response = dict()
    response["status_code"] = status_code

    if body is not None:
        response["body"] = json.dumps(body)

    return TransformDictionary.update_naming_convention(response, NamingConventions.SNAKE, NamingConventions.CAMEL)