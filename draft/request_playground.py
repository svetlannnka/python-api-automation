import requests
from datetime import datetime

user = {
  "username": "lanatest",
  "firstName": "Lana",
  "lastName": "Test",
  "email": f'test+{datetime.now().strftime("%m%d%Y%H%M%S")}@example.com',
  "password": "Password123!"
}

# POST /user
response = requests.post(url='https://playground.learnqa.ru/ajax/api/user', data=user)
print(response.status_code)
print(response.headers)
print(response.content)
print(f'Duration: {response.elapsed.total_seconds()} sec')
print(response.json())
print(response.json()['id'])
id = response.json()['id']

# POST /login
response = requests.post(url='https://playground.learnqa.ru/ajax/api/user/login',
                         data={'email': user['email'], 'password': 'Password123!'})
print(response.status_code)
print(response.headers)
print(response.headers['x-csrf-token'])
print(response.cookies.get('auth_sid'))

# GET /user/id
response = requests.get(url='https://playground.learnqa.ru/ajax/api/user/' + id,
                        headers={'x-csrf-token': response.headers['x-csrf-token']},
                        cookies={'auth_sid': response.cookies.get('auth_sid')},
                        data={'email': user['email'], 'password': 'Password123!'})
print(response.status_code)
if response.status_code == 200:
    print(response.headers)
    print(response.json())
