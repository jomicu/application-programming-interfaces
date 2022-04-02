from common.api import handle_request_body, handle_response

def handler(event, context):
    request_body: dict = handle_request_body(event["body"])

    # handle logic here
    user = request_body

    return handle_response(event, 201, build_response_body(user))


def build_response_body(token):
    return { "token": token }
