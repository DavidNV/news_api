import requests
import os
import json

class Collector:

    """
    News Collector. It's main function its to perform the main request to the news api and return the json value from it.
    """

    def __init__(self):
       self.api_key = self.__get_api_key__()
       self.url = 'https://newsapi.org/v2/top-headlines'

    def retrieve(self, country):
        params = {"country": country, "apiKey": self.api_key, "pageSize": 100}
        try:
            response = requests.get(self.url, params=params)
            json_response = response.json()
            return json_response
        except requests.exceptions.RequestException as e:
            #TODO Hey, future David, please don't forget to do something with the error. Best, present David.
            return self.__default_response__()

    def __get_api_key__(self):
        return os.environ['API_KEY']

    def __default_response__(self):
        return {"status": "unprocessable_entity", "totalResults": 0, "articles": []}
