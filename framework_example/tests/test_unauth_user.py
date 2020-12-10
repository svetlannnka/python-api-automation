# python -m pytest -s --alluredir=test_results/ framework_example/tests/test_unauth_user.py

import pytest
import allure
from framework_example.core.base_test import BaseCase
from framework_example.core.my_request import Request
from framework_example.core.asserts import Asserts


@allure.epic("Unauth cases")
class TestUnauthUser(BaseCase):
    users_provider = [
        ("1", "Lana"),
        ("2", "Vitaliy")
    ]

    @allure.description("This test is trying to get user data without id")
    def test_get_user_without_id(self):
        response = Request.get('user')

        Asserts.assert_code_status(response, 400)
        Asserts.assert_response_text(response, "Wrong HTTP method")
        Asserts.assert_time_is_less_than(response, 1)

    @allure.description("This test check username by user id")
    @pytest.mark.parametrize('user_id, name', users_provider)
    def test_get_user_with_id(self, user_id: str, name: str):
        response = Request.get(f'user/{user_id}')
        Asserts.assert_code_status(response, 200)
        Asserts.assert_json_value_by_key(response, "username", name)
        Asserts.assert_json_has_no_key(response, "firstName")
        Asserts.assert_json_has_no_key(response, "lastName")
        Asserts.assert_json_has_no_key(response, "email")

