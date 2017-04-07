import os

from django.core.wsgi import get_wsgi_application


os.environ["DJANGO_SETTINGS_MODULE"] = "dblpGraphs.config.settings"
application = get_wsgi_application()
from dblpGraphs.models import Author

import parser.pySaxParser


all_authors = Author.objects.all()
for a in all_authors:
    print(a.name, len([c.name for c in a.co_authors.all()]))