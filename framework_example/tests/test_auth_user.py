# python -m pytest -s --alluredir=test_results/ framework_example/tests/test_auth_user.py

from framework_example.core.base_test import BaseCase
from framework_example.core.my_request import Request
from framework_example.core.asserts import Asserts


class TestCreateUser(BaseCase):
    def test_wrong_data(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        response = Request.post('user/login', data)
        Asserts.assert_code_status(response, 400)
        Asserts.assert_response_text(response, "Invalid username/password supplied")
        Asserts.assert_response_not_has_cookie(response, 'auth_sid')
        Asserts.assert_response_not_has_headers(response, "x-csrf-token")

    def test_auth_successfully(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '123'
        }

        response = Request.post('user/login', data)
        Asserts.assert_code_status(response, 200)
        Asserts.assert_response_has_cookie(response, 'auth_sid')
        Asserts.assert_response_has_headers(response, "x-csrf-token")

    def test_get_user_with_id(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '123'
        }

        response = Request.post('user/login', data)

        Asserts.assert_json_has_key(response, 'user_id')

        auth_cookie = self.get_cookie(response, 'auth_sid')
        auth_header = self.get_header(response, 'x-csrf-token')
        user_id = response.json()['user_id']

        response = Request.get(f'user/{user_id}', headers=auth_header, cookies=auth_cookie)

        Asserts.assert_code_status(response, 200)
        Asserts.assert_json_has_key(response, 'firstName')
        Asserts.assert_json_has_key(response, 'lastName')
        Asserts.assert_json_has_key(response, 'email')

    def test_change_created_user_data(self):
        email = self.create_unique_email('vinkotov')
        password = '123'
        username = 'vinkotov'

        data = {
            'email': email,
            'password': password,
            'username': username,
            'firstName': 'Vitalii',
            'lastName': 'Kotov',
        }

        response = Request.post('user', data)
        user_id_after_registration = response.json()['id']

        response = Request.post('user/login', {'password': password, 'email': email})
        user_id_after_auth = response.json()['user_id']

        Asserts.assert_equals(user_id_after_registration, user_id_after_auth, "I've logged in as another user")

        auth_cookie = self.get_cookie(response, 'auth_sid')
        auth_header = self.get_header(response, 'x-csrf-token')

        response = Request.get(f'user/{user_id_after_auth}', headers=auth_header, cookies=auth_cookie)
        Asserts.assert_equals(username, response.json()['username'], "I've logged in as another user")

        new_user_name = "Vitaliy"
        response = Request.put(
            f'user/{user_id_after_auth}',
            data={'username': new_user_name},
            headers=auth_header,
            cookies=auth_cookie
        )
        Asserts.assert_code_status(response, 200)

        response = Request.get(f'user/{user_id_after_auth}', headers=auth_header, cookies=auth_cookie)
        Asserts.assert_equals(new_user_name, response.json()['username'], "Couldn't change name via put request")
