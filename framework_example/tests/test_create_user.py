# python -m pytest -s --alluredir=test_results/ framework_example/tests/test_create_user.py

from datetime import datetime
from framework_example.core.base_test import BaseCase
from framework_example.core.my_request import Request
from framework_example.core.asserts import Asserts


class TestCreateUser(BaseCase):
    def test_not_enough_data(self):
        response = Request.post('user')
        Asserts.assert_code_status(response, 400)
        Asserts.assert_response_text(response, "The following required params are missed: email, password, "
                                                        "username, firstName, lastName")

    def test_no_email(self):
        data = {
            'password': '123',
            'username': 'vinkotov',
            'firstName': 'Vitalii',
            'lastName': 'Kotov',
        }

        response = Request.post('user', data)
        Asserts.assert_code_status(response, 400)
        Asserts.assert_response_text(response, "The following required params are missed: email")

    def test_email_is_already_in_system(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '123',
            'username': 'vinkotov',
            'firstName': 'Vitalii',
            'lastName': 'Kotov',
        }

        response = Request.post('user', data)
        Asserts.assert_code_status(response, 400)
        Asserts.assert_response_text(response, f"Users with email '{data['email']}' already exists")

    def test_email_is_not_valid(self):
        data = {
            'email': 'vinkotov',
            'password': '123',
            'username': 'vinkotov',
            'firstName': 'Vitalii',
            'lastName': 'Kotov',
        }

        response = Request.post('user', data)
        Asserts.assert_code_status(response, 400)
        Asserts.assert_response_text(response, "Invalid email format")

    def test_username_is_too_short(self):
        data = {
            'email': f'test+{datetime.now().strftime("%m%d%Y%H%M%S")}@example.com',
            'password': '123',
            'username': 'v',
            'firstName': 'Vitalii',
            'lastName': 'Kotov',
        }

        response = Request.post('user', data)
        Asserts.assert_code_status(response, 400)
        Asserts.assert_response_text(response, "The value of 'username' field is too short")

    def test_create_user_successfully(self):
        data = {
            'email': f'test+{datetime.now().strftime("%m%d%Y%H%M%S")}@example.com',
            'password': '123',
            'username': 'vinkotov',
            'firstName': 'Vitalii',
            'lastName': 'Kotov',
        }

        response = Request.post('user', data)
        Asserts.assert_code_status(response, 200)
        Asserts.assert_json_has_key(response, "id")

