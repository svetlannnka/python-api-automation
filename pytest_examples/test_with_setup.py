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
            data={'email': self.created_user['email'], 'password': self.created_user['password']}
        )
        assert response.status_code == 200
        assert response.headers['x-csrf-token'] != ''
        assert response.cookies.get('auth_sid') != ''

    def test_login_user_incorrect_pw(self):
        response = requests.post(
            url='https://playground.learnqa.ru/ajax/api/user/login',
            data={'email': self.created_user['email'], 'password': 'Wrong Password123!'}
        )
        assert response.status_code == 400
        assert 'x-csrf-token' not in response.headers
        assert 'auth_sid' not in response.cookies.keys()
