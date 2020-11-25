import os
from support.logger import logger

"""
EXAMPLE OF PASSING ENVIRONMENT DYNAMICALLY
"""


class Environment:
    LOCAL = 'local'
    STAGING = 'staging'

    URLS = {
        LOCAL: 'http://localhost:8080',
        STAGING: 'https://playground.learnqa.ru/ajax/api/'
    }

    def __init__(self):
        self.name = self._get_environment_variable()

    @staticmethod
    def _get_environment_variable() -> str:
        try:
            return os.environ['ENVIRONMENT']
        except KeyError:
            logger.info('No variable passed, using default ENVIRONMENT: staging.')
            return 'staging'

    def base_url(self) -> str:
        return self.URLS[self.name]


ENV = Environment()
