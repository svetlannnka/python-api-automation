# python -m pytest -s --alluredir=test_results/ framework_example/tests/test_auth_user.py

from framework_example.core.base_test import BaseCase
from framework_example.core.my_request import Request
from framework_example.core.assertions_helper import AssertionsHelper


class TestCreateUser(BaseCase):
    def test_wrong_data(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        response = Request.post('user/login', data)
        AssertionsHelper.assert_code_status(response, 400)
        AssertionsHelper.assert_response_text(response, "Invalid username/password supplied")
        AssertionsHelper.assert_response_not_has_cookie(response, 'auth_sid')
        AssertionsHelper.assert_response_not_has_headers(response, "x-csrf-token")

    def test_auth_successfully(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '123'
        }

        response = Request.post('user/login', data)
        AssertionsHelper.assert_code_status(response, 200)
        AssertionsHelper.assert_response_has_cookie(response, 'auth_sid')
        AssertionsHelper.assert_response_has_headers(response, "x-csrf-token")

    def test_get_user_with_id(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '123'
        }

        response = Request.post('user/login', data)

        AssertionsHelper.assert_response_has_cookie(response, 'auth_sid')
        AssertionsHelper.assert_response_has_headers(response, "x-csrf-token")
        AssertionsHelper.assert_json_has_key(response, 'user_id')

        auth_cookie = self.get_cookie(response, 'auth_sid')
        auth_header = self.get_header(response, 'x-csrf-token')
        user_id = response.json()['user_id']

        response = Request.get(f'user/{user_id}', headers=auth_header, cookies=auth_cookie)

        AssertionsHelper.assert_code_status(response, 200)
        AssertionsHelper.assert_json_has_key(response, 'firstName')
        AssertionsHelper.assert_json_has_key(response, 'lastName')
        AssertionsHelper.assert_json_has_key(response, 'email')






