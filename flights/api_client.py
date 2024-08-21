# В данном файле будут описаны функции для обращения к Aviasales API.

from django.conf import settings
import requests
import yaml
from pathlib import Path

API_TOKEN = settings.config['api_key_aviasales']
BASE_URL_V1 = 'https://api.travelpayouts.com/v1/'
BASE_URL_V2 = 'https://api.travelpayouts.com/v2/'


class AviasalesConnectV1:
    def __init__(self):
        self.api_key = API_TOKEN
        self.base_url = BASE_URL_V1


class AviasalesConnectV2:
    def __init__(self):
        self.api_key = API_TOKEN
        self.base_url = BASE_URL_V2
