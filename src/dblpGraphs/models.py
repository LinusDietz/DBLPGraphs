import os

from django.core.wsgi import get_wsgi_application
from django.db import models

os.environ["DJANGO_SETTINGS_MODULE"] = "dblpGraphs.config.settings"
application = get_wsgi_application()


class Author(models.Model):
    name = models.CharField()
