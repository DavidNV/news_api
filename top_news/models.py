from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField
    url = models.CharField(max_length=255)
    url_to_image = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateField
    content = models.TextField

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('published_at',)

class Author(models.Model):
    name = models.CharField(max_length=255)
    articles = models.ManyToManyField(Article)

    def __str__(self):
        return self.name

class Source(models.Model):
    uid = models.CharField(max_length=70)
    name = models.CharField(max_length=200)
    articles = models.ManyToManyField(Article)
    authors = models.ManyToManyField(Author)
