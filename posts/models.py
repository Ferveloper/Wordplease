import datetime

from django.db import models
from django.contrib.auth.models import User
from django.db.models import ForeignKey


class Category(models.Model):
    
    class Meta:
        verbose_name_plural = "categories"

    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Post(models.Model):

    title = models.CharField(max_length=150)
    url = models.URLField()
    introduction = models.TextField()
    body = models.TextField()
    publication_date = models.DateTimeField(default=datetime.datetime.now)
    creation_date = models.DateTimeField(auto_now_add=True)
    modification_date = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(Category)
    owner = ForeignKey(User, related_name='posts', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
