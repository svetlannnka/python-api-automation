# python -m pytest -s --alluredir=test_results/ framework_example/tests/test_unauth_user.py

import pytest
from framework_example.core.base_test import BaseCase
from framework_example.core.my_request import Request
from framework_example.core.assertions_helper import AssertionsHelper


class TestUnauthUser(BaseCase):
    def test_get_user_without_id(self):
        response = Request.get('user')
        AssertionsHelper.assert_code_status(response, 400)
        AssertionsHelper.assert_response_text(response, "Wrong HTTP method")

    @pytest.mark.parametrize('id, name', [("1", "Lana"), ("2", "Vinkotov")])
    def test_get_user_with_id(self, id: str, name: str):
        response = Request.get(f'user/{id}')
        AssertionsHelper.assert_code_status(response, 200)
        AssertionsHelper.assert_json_value_by_key(response, "username", name)
        AssertionsHelper.assert_json_has_no_key(response, "firstName")
        AssertionsHelper.assert_json_has_no_key(response, "lastName")
        AssertionsHelper.assert_json_has_no_key(response, "email")

