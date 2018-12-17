import requests
import os
import json

class Collector:

    def __init__(self):
       self.api_key = self.__get_api_key__()
       self.url = 'https://newsapi.org/v2/top-headlines'

    def retrieve(self, country="us"):
        params = {"country": country, "apiKey": self.api_key, "pageSize": 100}
        response = requests.get(self.url, params=params)
        json_response = response.json()
        return json_response

    def __get_api_key__(self):
        return os.environ['API_KEY']
