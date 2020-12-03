import os


class Environment:
    DEV = 'dev'
    PROD = 'prod'

    URLS = {
        DEV: 'https://playground.learnqa.ru/ajax/api_dev/',
        PROD: 'https://playground.learnqa.ru/ajax/api/'
    }

    def __init__(self):
        self.name = self._get_environment_variable()

    @classmethod
    def _get_environment_variable(cls) -> str:
        try:
            return os.environ['ENVIRONMENT']
        except KeyError:
            return cls.DEV

    def base_url(self) -> str:
        return self.URLS[self.name]


ENV = Environment()
