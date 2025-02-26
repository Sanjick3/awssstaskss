import json
from commons.log_helper import get_logger
from commons.abstract_lambda import AbstractLambda

_LOG = get_logger(__name__)


class HelloWorld(AbstractLambda):

    def validate_request(self, event) -> dict:
        """
        Placeholder for request validation logic.
        """
        return {}

    def handle_request(self, event, context):
        """
        Process incoming Lambda requests and route them accordingly.
        """
        method = event.get("requestContext", {}).get("http", {}).get("method", "UNKNOWN")
        route = event.get("rawPath", "/")

        if method == "GET" and route == "/hello":
            response_body = {
                "statusCode": 200,
                "message": "Hello from Lambda"
            }
            status_code = 200
        else:
            response_body = {
                "statusCode": 400,
                "message": f"Bad request syntax or unsupported method. Request path: {route}. HTTP method: {method}"
            }
            status_code = 400

        return {
            "statusCode": status_code,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps(response_body)
        }


HANDLER = HelloWorld()


def lambda_handler(event, context):
    return HANDLER.lambda_handler(event=event, context=context)
