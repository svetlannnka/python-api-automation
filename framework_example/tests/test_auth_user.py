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

    def test_get_auth_data(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '123'
        }

        response = Request.post('user/login', data)
        AssertionsHelper.assert_code_status(response, 200)
        AssertionsHelper.assert_response_text(response, "")
        AssertionsHelper.assert_response_has_cookie(response, 'auth_sid')
        AssertionsHelper.assert_response_has_headers(response, "x-csrf-token")




