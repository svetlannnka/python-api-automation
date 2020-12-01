import requests
from datetime import datetime

from support.environment import ENV

# TODO: examples of GET and basic API calls


user = {
  "username": "lanatest",
  "firstName": "Lana",
  "lastName": "Test",
  "email": f'test+{datetime.now().strftime("%m%d%Y%H%M%S")}@example.com',
  "password": "Password123!"
}

# Post /user
r = requests.post(url="https://playground.learnqa.ru/ajax/api/user", data=user)
print(r.status_code)
print(r.json())
print(r.headers)

url = f'{ENV.base_url()}/user'
