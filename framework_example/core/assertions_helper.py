import allure
import json
from requests import Response


class AssertionsHelper:
    @staticmethod
    def assert_code_status(response: Response, expected_code: int, message: str = ""):
        assert response.status_code == expected_code, \
            f'Expected status code {expected_code}, but got {response.status_code}. {message}'

    @staticmethod
    def assert_response_text(response: Response, expected_text: str, message: str = ""):
        assert response.text == expected_text, \
            f'Expected response text "{expected_text}", but got "{response.text}". {message}'

    @staticmethod
    def assert_json_value_by_key(response: Response, key: str, val: str):
        try:
            response_as_dict = response.json()
        except json.decoder.JSONDecodeError:
            assert False, f'Response is not in JSON format. Response text is "{response.text}"'

        assert key in response_as_dict, \
            f'Response json does\'n have key "{key}"'

        assert response_as_dict[key] == val, \
            f'Response key "{key}" has value {response_as_dict[key]} but expected is {val}'

    @staticmethod
    def assert_json_has_key(response: Response, key: str):
        try:
            response_as_dict = response.json()
        except json.decoder.JSONDecodeError:
            assert False, f'Response is not in JSON format. Response text is "{response.text}"'

        assert key in response_as_dict, \
            f'Response json does not have a key "{key}" which is expected. JSON text: "{response.text}"'

    @staticmethod
    def assert_json_has_no_key(response: Response, key: str):
        try:
            response_as_dict = response.json()
        except json.decoder.JSONDecodeError:
            assert False, f'Response is not in JSON format. Response text is "{response.text}"'

        assert key not in response_as_dict, \
            f'Response json has key "{key}" which is not expected.'

    @staticmethod
    def assert_response_has_headers(response: Response, key: str):
        assert key in response.headers, \
            f'Cannot find header with name {key} in the response. All headers in the response: ' \
            + str(response.headers)

    @staticmethod
    def assert_response_not_has_headers(response: Response, key: str):
        assert key not in response.headers, \
            f'Found header with name {key} in the response which is not expected.'

    @staticmethod
    def assert_response_has_cookie(response: Response, name):
        cookies = response.cookies
        assert name in cookies, \
            f'Cannot find cookie with name {name} in the response. All cookies in the response: ' \
            + AssertionsHelper._get_cookies(response.cookies)

    @staticmethod
    def assert_response_not_has_cookie(response: Response, name):
        cookies = response.cookies
        assert name not in cookies, \
            f'Found cookie with name {name} in the response which is not expected.' \
            + AssertionsHelper._get_cookies(response.cookies)

    @staticmethod
    def _get_cookies(cookie_jar):
        domain = '.playground.learnqa.ru'
        cookie_dict = cookie_jar.get_dict(domain=domain)
        found = ['%s=%s' % (name, value) for (name, value) in cookie_dict.items()]
        return ';'.join(found)
