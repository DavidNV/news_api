import re
from datetime import datetime
from top_news.models import *

class Creator:

    def __init__(self, data):
        self.data = data

    def persist(self):
      for article in self.data:
          self.__path_from_source__(article)

    def __path_from_source__(self, article_data):
        source_info = article_data.pop("source")
        current_source = Source.objects.get_or_create(uid = source_info["id"], name = source_info["name"])[0]
        self.__set_author_for_source__(current_source, article_data)

    def __set_author_for_source__(self, source, article_data):
        author = Author.objects.get_or_create(name= str(article_data.pop("author")))[0]
        source.author = author
        source.save()
        self.__set_article_for_author__(author, article_data)

    def __set_article_for_author__(self, _author, article_data):
        self.__prepare_article_params__(_author, article_data)
        Article.objects.get_or_create(**article_data)

    def __prepare_article_params__(self, _author, article_data):
        date = article_data.pop("publishedAt")
        clean_date = self.__parse_date__(date)

        article_data["published_at"] =  clean_date
        article_data["url_to_image"] = article_data.pop("urlToImage")
        article_data["author"] = _author


    def __parse_date__(self, date):
        regex = re.compile("[^0-9]")
        data = regex.split(date)[:-1]
        return datetime(*[int(x) for x in data])
