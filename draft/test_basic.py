import requests
import pytest


class TestBasic:
    names = ['', 'Vasya', 'Another Name R2-D2']

    @pytest.mark.parametrize('name', names)
    def test_hello(self, name):
        response = requests.get(url=f'https://playground.learnqa.ru/ajax/api/hello?name={name}')
        assert response.status_code == 200
        assert response.elapsed.total_seconds() < 10
        assert response.content.decode() == f'Hello, {name}'
