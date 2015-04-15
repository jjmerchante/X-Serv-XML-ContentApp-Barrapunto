from django.db import models

# Create your models here.


class Page(models.Model):
    name = models.CharField(max_length=128)
    page = models.TextField()


class News(models.Model):
    content = models.TextField()
