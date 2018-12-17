from top_news.lib.collector import Collector
from top_news.lib.creator import Creator

class Builder:

    def __init__(self):
        self.collector = Collector()
        self.global_response = {"total": 0, "articles": []}

    def build(self):
        self.__get_news__()
        Creator(self.global_response["articles"]).persist()

    def __get_news__(self):
        countries = ["us", "jp", "co", "ru", "gb"]
        for country in countries:
            print(self.global_response["total"])
            if self.global_response["total"] < 100:
                _news = self.collector.retrieve(country)
                self.__add_to_global_response__(_news)

    def __add_to_global_response__(self, _news):
        if _news["status"] == 'ok':
            self.global_response["total"] += _news["totalResults"]
            self.global_response["articles"] += _news["articles"]

