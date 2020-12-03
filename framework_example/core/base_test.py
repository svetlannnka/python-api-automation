import allure
from requests import Response
from framework_example.environment import ENV
from framework_example.core.logger import Logger


class BaseCase:
    def setup(self):
        pass

    def teardown(self):
        Logger.get_instance().write_log_to_file()
        Logger.get_instance().clear_data()

    @staticmethod
    def get_cookie(response: Response, cookie_name):
        if cookie_name in response.cookies:
            return {cookie_name: response.cookies[cookie_name]}
        else:
            raise Exception(f"Cannot get cookie with name {cookie_name} from the last response")

    @staticmethod
    def base_url() -> str:
        return ENV.base_url()
