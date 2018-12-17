from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True)
    url = models.CharField(max_length=255)
    url_to_image = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateField()
    content = models.TextField(null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Source(models.Model):
    uid = models.CharField(max_length=70, null=True)
    name = models.CharField(max_length=200)
    articles = models.ManyToManyField(Article)
