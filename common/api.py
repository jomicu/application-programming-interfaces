from logging import INFO, getLogger
import json

from common.enums import NamingConventions
from common.transform import TransformDictionary

logger = getLogger()
logger.setLevel(INFO)

def handle_request(request: dict) -> dict:
    logger.info(f"Received request: {json.dumps(request)}")
    request["queryStringParameters"] = TransformDictionary.update_naming_convention(request["queryStringParameters"], NamingConventions.CAMEL, NamingConventions.SNAKE)
    request["pathParameters"] = TransformDictionary.update_naming_convention(request["pathParameters"], NamingConventions.CAMEL, NamingConventions.SNAKE)
    request["body"] = TransformDictionary.update_naming_convention(request["body"], NamingConventions.CAMEL, NamingConventions.SNAKE)
    logger.info(f"Received (transformed) requesy: {json.dumps(request)}")
    return request


# TODO cors and headers
def handle_response(event: dict, status_code: int, body: dict = None):
    valid_cors_origins = ""
    headers = ""
    
    response = dict()
    response["status_code"] = status_code

    if body is not None:
        response["body"] = body

    logger.info(f"Response to be sent: {json.dumps(response)}")
    transformed_response = TransformDictionary.update_naming_convention(response, NamingConventions.SNAKE, NamingConventions.CAMEL)
    logger.info(f"Sending (transformed) response: {json.dumps(transformed_response)}")

    transformed_body = transformed_response.get("body", None)
    if transformed_body is not None:
        transformed_response["body"] = json.dumps(transformed_body)

    return transformed_response