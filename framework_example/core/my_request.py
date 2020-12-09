import requests
from framework_example.core.logger import Logger
from framework_example.environment import ENV


class Request:
    @staticmethod
    def post(url: str, data: dict = None, headers: dict = None, cookies: dict = None):
        return Request._send(url, data, headers, cookies, 'POST')

    @staticmethod
    def get(url: str, data: dict = None, headers: dict = None, cookies: dict = None):
        return Request._send(url, data, headers, cookies, 'GET')

    @staticmethod
    def put(url: str, data: dict = None, headers: dict = None, cookies: dict = None):
        return Request._send(url, data, headers, cookies, 'PUT')

    @staticmethod
    def _send(url: str, data: dict, headers: dict, cookies: dict, method: str):
        url = f"{ENV.base_url()}{url}"

        if headers is None:
            headers = {}

        if cookies is None:
            cookies = {}

        additional_header = {'X-THIS_IS_TEST': 'True'}
        headers.update(additional_header)

        Logger.get_instance().add_request(url, data, headers, cookies, method)

        if method == 'GET':
            response = requests.get(url, params=data, headers=headers, cookies=cookies)
        elif method == 'POST':
            response = requests.post(url, data=data, headers=headers, cookies=cookies)
        elif method == 'PUT':
            response = requests.put(url, data=data, headers=headers, cookies=cookies)
        else:
            raise Exception(f'Bad HTTP method "{method}" was received')

        Logger.get_instance().add_response(response)
        return response
