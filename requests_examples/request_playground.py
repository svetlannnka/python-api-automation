import requests
from datetime import datetime

"""
https://playground.learnqa.ru/ajax/api/map
"""

# example of GET and basic API call
# response = requests.get(url='https://playground.learnqa.ru/ajax/api/hello')
# print(response.status_code)
# print(response.text)
# print(response.headers)
# print(response.headers['Date'])

# example of POST and basic API calls
# response = requests.post(url='https://playground.learnqa.ru/ajax/api/check_type')
# print(response.status_code)
# print(response.text)

# example of JSON
# response = requests.get(url='https://playground.learnqa.ru/ajax/api/get_json')
# print(response.status_code)
# print(response.json())
# print(response.json()['name'])
# print(response.json()['fname'])

# example of a cookie
# response = requests.get(url='https://playground.learnqa.ru/ajax/api/get_cookie')
# print(response.status_code)
# print(response.headers)
# print(response.cookies.get('MyCookie'))

# example of POST with payload, POST /user
# user = {
#   "username": "lanatest",
#   "firstName": "Lana",
#   "lastName": "Test",
#   "email": f'test+{datetime.now().strftime("%m%d%Y%H%M%S")}@example.com'
# }
#
# response = requests.post(url="https://playground.learnqa.ru/ajax/api/user", data=user)
# print(response.status_code)
# print(response.text)
