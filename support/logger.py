import logging
import os

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

path = os.path.abspath(os.path.join(os.getcwd(), '../api_automation.log'))
handler = logging.FileHandler(path)
handler.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


def clean_log_file(file='api_automation.log'):
    open(file, 'w').close()


def log_response(method, response):
    logger.info('{} Status Code: {}'.format(method, response.status_code))
    logger.info('{} Response content: {}'.format(method, response.content))
    logger.info(f'Response headers: {response.headers}')
