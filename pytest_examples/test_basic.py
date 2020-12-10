# python3 -m pytest pytest_examples/test_basic.py

import requests
from datetime import datetime


class TestBasic:

    def test_post_user(self):
        user = {
            'username': 'lanatest',
            'password': 'Password123!',
            'firstName': 'Lana',
            'lastName': 'Test',
            'email': f'test+{datetime.now().strftime("%m%d%Y%H%M%S")}@example.com'
        }
        response = requests.post(url='https://playground.learnqa.ru/ajax/api/user', data=user)
        assert response.status_code == 200, f'Expected status code 200, but got {response.status_code}'
        assert response.json()['id'] != ''
        assert response.elapsed.total_seconds() < 5

    def test_user_login(self):
        username, password = 'lanatest', 'Password123!'
        email = f'test+{datetime.now().strftime("%m%d%Y%H%M%S")}@example.com'
        user = {
            'username': username,
            'password': password,
            'firstName': 'Lana',
            'lastName': 'Test',
            'email': email,
        }
        requests.post(url='https://playground.learnqa.ru/ajax/api/user', data=user)
        response = requests.post(
            url='https://playground.learnqa.ru/ajax/api/user/login',
            data={'email': email, 'password': password}
        )
        assert response.status_code == 200
        assert response.headers['x-csrf-token'] != ''
        assert response.cookies.get('auth_sid') != ''
