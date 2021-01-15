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