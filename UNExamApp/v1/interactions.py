import requests
from json import loads, dumps
import os
from UNExamApp.settings import BaseURL
from UNExamApp.exceptions import EscwaException
from UNExamApp.logger import logger



def send_request(endpoint, method, headers={}, payload = {}):
    path =  BaseURL + endpoint
    logger.info("Sending request to: {}".format(path))
    logger.info("Headers: {}".format(headers))
    logger.info("Body: {}".format(payload))
    response = requests.request(method, path, headers=headers, data=dumps(payload))
    if response.status_code not in [200, 201]:
        raise EscwaException("server_error", "Escwa API did not return 200")
    return loads(response.text)