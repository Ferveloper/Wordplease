from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):

    TECHNOLOGY = 'TEC'
    STARTUPS = 'STA'
    HEALTH = 'HEA'
    POLITICS = 'POL'

    CATEGORIES = [
        [TECHNOLOGY, 'Tecnología'],
        [STARTUPS, 'Startups'],
        [HEALTH, 'Salud'],
        [POLITICS, 'Politica']
    ]

    title = models.CharField(max_length=150)
    url = models.URLField()
    introduction = models.TextField()
    body = models.TextField()
    publication_date = models.DateTimeField()
    creation_date = models.DateTimeField(auto_now_add=True)
    modification_date = models.DateTimeField(auto_now=True)
    categories = models.CharField(max_length=3, choices=CATEGORIES)
    # author = models.CharField(max_length=30)

    def __str__(self):
        return self.name
