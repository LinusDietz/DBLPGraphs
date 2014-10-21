from django.conf.urls import patterns, url
from django.conf import settings
from django.conf.urls.static import static
import dblpGraphs.pySaxParser as p
import statsUtil

class Stats:
    def __init__(self):
        self.topAuthors = statsUtil.topAuthors(db, 15)
        self.topCoAuthors = statsUtil.topCoAuthors(db, 15)
        self.mean = statsUtil.publicationsMean(db)
        self.var = statsUtil.publicationsVar(db)
        self.median = statsUtil.publicationsMedian(db)
        self.mode = statsUtil.publicationsMode(db)
        coaStats = statsUtil.coAuthorStats(db)
        self.coaMean = coaStats[0]
        self.coaVar= coaStats[1]
        self.coaMedian = coaStats[2]
        self.coaMode= coaStats[3]
        self.publications = statsUtil.publicationsDistribution(db)

db = p.ch
stats = Stats()


urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'dblpGraphs.views.home', name='home'),
    url(r'^coauthors$', 'dblpGraphs.views.coAuthors', name='coAauthors'),
    url(r'^coauthorspdf$', 'dblpGraphs.views.coAuthorsPDF', name='coAauthorspdf'),
    url(r'^coauthors2pdf$', 'dblpGraphs.views.coAuthors2PDF', name='coAauthor2spdf'),

) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 

