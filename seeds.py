from top_news.models import *
from top_news.lib.builder import Builder

Author.objects.all().delete()
Article.objects.all().delete()
Source.objects.all().delete()

b = Builder()
b.build()
