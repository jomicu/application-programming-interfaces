import json


from common.transformers.dictionary_parser import DictionaryParser


def handle_request_body(body: str):
    parser = DictionaryParser(parse_to_snake_case=True)
    return parser.parse(json.loads(body))

def handle_response(event: dict, status_code: int, body: dict = None):
    valid_cors_origins = ""
    headers = ""
    
    response = { 
        "statusCode": status_code 
    }

    if body is not None:
        response["body"] = json.dumps(body)

    return response