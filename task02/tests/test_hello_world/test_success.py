from tests.test_hello_world import HelloWorldLambdaTestCase

class TestHelloWorldLambda(HelloWorldLambdaTestCase):

    def test_hello_success(self):
        event = {
            "requestContext": {
                "http": {
                    "method": "GET"
                }
            },
            "rawPath": "/hello"
        }
        response = self.HANDLER.handle_request(event, {})

        assert response["statusCode"] == 200
        body = json.loads(response["body"])
        assert body["message"] == "Hello from Lambda"

    def test_bad_request(self):
        event = {
            "requestContext": {
                "http": {
                    "method": "GET"
                }
            },
            "rawPath": "/invalid_path"
        }
        response = self.HANDLER.handle_request(event, {})

        assert response["statusCode"] == 400
        body = json.loads(response["body"])
        assert body["message"] == "Bad request syntax or unsupported method. Request path: /invalid_path. HTTP method: GET"
