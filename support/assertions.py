import allure
import jsonref

from jsonschema import validate

from os.path import dirname, join


@allure.step('Returned JSON schema is correct')
def assert_valid_schema(data, schema_file):
    """
    Verifies that the given data matches the JSON schema
    """
    schema_base_dir = join(dirname(dirname(__file__)), 'support/schemas')
    schema_file_path = f'{schema_base_dir}/{schema_file}'
    base_uri = f'file://{schema_base_dir}/'

    with open(schema_file_path) as schema_file:
        schema = jsonref.loads(schema_file.read(), base_uri=base_uri, jsonschema=True)
        return validate(data, schema)


@allure.step('Returned Status Code is {expected_code}')
def assert_status_code(response, expected_code, message=''):
    assert response.status_code == expected_code, \
            f'Expected status code {expected_code}, but got {response.status_code}. {message}\n{response.json()}'


@allure.step('Response time is less than {max_time} sec')
def assert_max_response_time(response, max_time):
    response_time = response.elapsed.total_seconds()
    assert response_time < max_time, f'Expected response time < {max_time} s, but actual is {response_time} s'


@allure.step('Response body contains {expected_key} set to {expected_value}')
def assert_response_key_value(response, expected_key, expected_value):
    """
    Verifies a value returned in response's body
    :param response: response.json()
    :param expected_key: expected key from response body
    :param expected_value: expected value for the key from response body
    """
    assert response.json()[expected_key] == expected_value,  \
        f'Expected {expected_key} to be {expected_value}, but got {response.json()[expected_key]}'
