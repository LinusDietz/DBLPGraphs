import os

from django.core.wsgi import get_wsgi_application
from django.db import models




class Author(models.Model):
    name = models.CharField(max_length=100, unique=True)
    co_authors = models.ManyToManyField("self")

