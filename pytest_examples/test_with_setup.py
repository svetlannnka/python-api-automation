import requests
from datetime import datetime


class TestWithSetup:
    user_id: str = ''
    created_user: dict = ''

    @staticmethod
    def generate_user():
        user = {
            'username': 'lanatest',
            'password': 'Password123!',
            'firstName': 'Lana',
            'lastName': 'Test',
            'email': f'test+{datetime.now().strftime("%m%d%Y%H%M%S")}@example.com'
        }
        return user

    def setup_method(self):
        self.created_user = self.generate_user()
        response = requests.post(url='https://playground.learnqa.ru/ajax/api/user', data=self.created_user)
        assert response.status_code == 200
        self.user_id = response.json()['id']

    def test_login_user(self):
        response = requests.post(
            url='https://playground.learnqa.ru/ajax/api/user/login',
            data={'username': self.created_user['username'], 'password': self.created_user['password']}
        )
        assert response.status_code == 200
        assert response.headers['x-csrf-token'] != ''
        assert response.cookies.get('auth_sid') != ''

    def test_get_user(self):
        response = requests.post(
            url='https://playground.learnqa.ru/ajax/api/user/login',
            data={'username': self.created_user['username'], 'password': self.created_user['password']}
        )
        # TODO: get headers
        response = requests.get(
            url=f'https://playground.learnqa.ru/ajax/api/user/{self.user_id}',
            # TODO: add headers
        )
        assert response.status_code == 200
