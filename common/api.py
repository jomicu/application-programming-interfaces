from logging import info, getLogger
import json

from common.enums import NamingConventions
from common.transform import TransformDictionary

logger = getLogger()
logger.setLevel(info())

def handle_request_body(body: str):
    body = json.loads(body)
    logger.info(f"Received request_body: {json.dumps(body)}")
    transformed_body = TransformDictionary.update_naming_convention(body, NamingConventions.CAMEL, NamingConventions.SNAKE)
    logger.info(f"Received (transformed) request_body: {json.dumps(transformed_body)}")
    return transformed_body

# TODO cors and headers
def handle_response(event: dict, status_code: int, body: dict = None):
    valid_cors_origins = ""
    headers = ""
    
    response = dict()
    response["status_code"] = status_code

    if body is not None:
        response["body"] = json.dumps(body)

    logger.info(f"Response to be sent: {json.dumps(response)}")
    transformed_response = TransformDictionary.update_naming_convention(response, NamingConventions.SNAKE, NamingConventions.CAMEL)
    logger.info(f"Sending (transformed) response: {json.dumps(transformed_response)}")

    return transformed_response