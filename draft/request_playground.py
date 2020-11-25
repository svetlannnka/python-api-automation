import requests

user = {
  "username": "lanatest",
  "firstName": "Lana",
  "lastName": "Test",
  "email": "test112410@example.com",
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

# POST /login
response = requests.post(url='https://playground.learnqa.ru/ajax/api/user/login',
                         data={'username': 'lanatest', 'password': 'Password123!'})
print(response.status_code)
print(response.headers)
print(response.headers['X-CSRF-TOKEN'])
print(response.cookies.get('auth_sid'))

# GET /user/id
response = requests.get(url='https://playground.learnqa.ru/ajax/api/user/3',
                        # TODO headers = {'x-csrf-token': c, 'X-Session-Id': t},
                        data={'username': 'lanatest', 'password': 'Password123!'})
print(response.status_code)
print(response.headers)
print(response.json())
