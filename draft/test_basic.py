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
        assert response.elapsed.total_seconds() < 2

    def test_user_login(self):
        username, password = 'lanatest', 'Password123!'
        user = {
            'username': username,
            'password': password,
            'firstName': 'Lana',
            'lastName': 'Test',
            'email': f'test+{datetime.now().strftime("%m%d%Y%H%M%S")}@example.com',
        }
        requests.post(url='https://playground.learnqa.ru/ajax/api/user', data=user)
        response = requests.post(
            url='https://playground.learnqa.ru/ajax/api/user/login',
            data={'username': username, 'password': password}
        )
        assert response.status_code == 200
        assert response.headers['x-csrf-token'] != ''
        assert response.cookies.get('auth_sid') != ''

    def test_user_get(self):
        username, password = 'lanatest', 'Password123!'
        user = {
            'username': username,
            'password': password,
            'firstName': 'Lana',
            'lastName': 'Test',
            'email': f'test+{datetime.now().strftime("%m%d%Y%H%M%S")}@example.com',
        }
        response = requests.post(url='https://playground.learnqa.ru/ajax/api/user', data=user)
        user_id = response.json()['id']
        requests.post(
            url='https://playground.learnqa.ru/ajax/api/user/login',
            data={'username': username, 'password': password}
        )
        response = requests.get(url=f'https://playground.learnqa.ru/ajax/api/user/{user_id}',
                                # TODO add headers
                                data={'username': username, 'password': password})
        assert response.status_code == 200
        assert response.json()['username'] == user['username']
        assert response.json()['firstName'] == user['firstName']
        assert response.json()['lastName'] == user['lastName']
        assert response.json()['email'] == user['email']
