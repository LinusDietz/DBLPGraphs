from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from dblpGraphs import views


urlpatterns = [
               url(r'^$', views.home, name='home'),
               url(r'^coauthors$', views.coAuthors, name='coauthors'),
               url(r'^coauthorspdf$', views.coAuthorsPDF),
               url(r'^coauthors2pdf$', views.coAuthors2PDF),
               ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
