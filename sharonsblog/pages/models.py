from django.db import models
from datetime import datetime 

class Article(models.Model):
    title = models.CharField(max_length = 100)
    image1 = models.CharField(max_length = 500)
    short = models.CharField(max_length = 200)
    desc = models.TextField(max_length = 2000)
    author = models.CharField(max_length = 100)
    category1 = models.CharField(max_length = 100)
    category2 = models.CharField(max_length = 100, blank =True)
    category3 = models.CharField(max_length = 100, blank = True)
    date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.title 

class Podcast(models.Model):
    title = models.CharField(max_length = 100)
    link = models.CharField(max_length = 300)
    short = models.CharField(max_length = 200)
    author = models.CharField(max_length = 100)
    date = models.DateTimeField(default=datetime.now, blank=True)
    category = models.CharField(max_length = 100)
    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length = 100)
    email = models.CharField(max_length = 300)
    website = models.CharField(max_length = 200, blank =True)
    message = models.TextField(max_length = 2000)
    def __str__(self):
        return self.name


