from django.shortcuts import render
from django.http import HttpResponse

from dblpGraphs.models import Author
from . import printUtil
import random
import urllib.request
import urllib.parse
import urllib.error


# Main page
def home(request):
    random_author = random.choice(list(Author.objects.all()))
    co_authors = random_author.co_authors.all()
    #while len(co_authors) < 10 or len(co_authors) > 100:
    #    random_author = random.choice(list(Author.objects.all()))
    return render(request, 'index.html', {'db' : len(Author.objects.all()), 'randomAuthor' : random_author.name }, )


# Search results
def coAuthors(request):
    msg = "Please enter a valid search term!"
    if 'q' in request.GET and request.GET['q']:
        q= request.GET['q']
        if not q:
            msg = "Please enter a search term!"
            return render(request, 'search.html', {'msg': msg})
        else:
            try:
                author = Author.objects.get(name=q)
                printUtil.printSFDPa(q)
                image = printUtil.outputPath("coadb_connected_", q) + ".png"
                return render(request, 'search_results.html',
                              {'coAuthors': author.co_authors.all(), 'query': q, 'image': image})
            except:
                msg = "'%s' was not found in the database. Please enter the exact name of the author!" % q
                return render(request, 'search.html', {'msg': msg, 'query': q})
    else:
        return render(request, 'search.html', {'msg': msg})


# Returns the level-1 PDF
def coAuthorsPDF(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        if not q:
            msg = "Please enter a search term!"
            return render(request, 'search.html', {'msg': msg})
        else:
            printUtil.printSFDPaPDF(q)
            mypdf = 'dblpGraphs/static/output/coadb_connected_' + q + '.sfdp.pdf'
            with open(mypdf, 'r') as pdf:
                # response = HttpResponse(pdf.read(), mimetype='application/pdf')
                response = HttpResponse(content_type='application/pdf')
                response['Content-Disposition'] = 'inline;filename=%s.pdf' % ("Coauthors of " + u)
            return response


# Returns the level-2 PDF
def coAuthors2PDF(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        if not q:
            msg = "Please enter a search term!"
            return render(request, 'search.html', {'msg': msg})
        else:
            printUtil.printSFDP2PDF(q)
            mypdf = 'dblpGraphs/static/output/coadb_coauthors_' + printUtil.pathEsc(q) + '.sfdp.pdf'
            with open(mypdf, 'r') as pdf:
                # response = HttpResponse(pdf.read(), mimetype='application/pdf')
                response = HttpResponse(content_type='application/pdf')
                response['Content-Disposition'] = 'inline;filename=%s.pdf' % ("Coauthors of coauthors of " + u)
            return response
