from django.shortcuts import render
from django.http import HttpResponse

from . import printUtil
import random
import urllib.request
import urllib.parse
import urllib.error


# Main page
def home(request):
    randomAuthor = random.choice(list(db.coauthorsDB.keys()))
    while len(db.coauthorsDB[randomAuthor]) < 10 or len(db.coauthorsDB[randomAuthor]) > 100:
        randomAuthor = random.choice(list(db.coauthorsDB.keys()))
    return render(request, 'index.html',
                  {'db': len(db.coauthorsDB), 'stats': stats, 'randomAuthor': urllib.parse.unquote(randomAuthor)}, )


# Search results
def coAuthors(request):
    msg = "Please enter a valid search term!"
    if 'q' in request.GET and request.GET['q']:
        q = urllib.parse.quote(request.GET['q'].encode('utf8'))
        u = urllib.parse.unquote(q)
        if not q:
            msg = "Please enter a search term!"
            return render(request, 'search.html', {'msg': msg})
        else:
            try:
                coAuthors_raw = db.coauthorsDB[q]
                coAuthors1 = []
                for coa in coAuthors_raw:
                    coAuthors1.append((urllib.parse.unquote(coa), db.coauthorsDB[q][coa]))
                printUtil.printSFDPa(db, q)
                image = 'output/coadb_connected_' + printUtil.pathEsc(u) + '.sfdp.png'
                # image = printUtil.outputPath("coadb_connected_", q) + ".png"
                return render(request, 'search_results.html',
                              {'coAuthors': coAuthors1, 'query': urllib.parse.unquote(q), 'image': image})
            except:
                msg = "'%s' was not found in the database. Please enter the exact name of the author!" % u
                return render(request, 'search.html', {'msg': msg, 'query': u})
    else:
        return render(request, 'search.html', {'msg': msg})


# Returns the level-1 PDF
def coAuthorsPDF(request):
    if 'q' in request.GET and request.GET['q']:
        q = urllib.parse.quote(request.GET['q'].encode('utf8'))
        u = urllib.parse.unquote(q)
        if not q:
            msg = "Please enter a search term!"
            return render(request, 'search.html', {'msg': msg})
        else:
            printUtil.printSFDPaPDF(db, q)
            mypdf = 'dblpGraphs/static/output/coadb_connected_' + printUtil.pathEsc(u) + '.sfdp.pdf'
            with open(mypdf, 'r') as pdf:
                # response = HttpResponse(pdf.read(), mimetype='application/pdf')
                response = HttpResponse(content_type='application/pdf')
                response['Content-Disposition'] = 'inline;filename=%s.pdf' % ("Coauthors of " + u)
            return response


# Returns the level-2 PDF
def coAuthors2PDF(request):
    if 'q' in request.GET and request.GET['q']:
        q = urllib.parse.quote(request.GET['q'].encode('utf8'))
        u = urllib.parse.unquote(q)
        if not q:
            msg = "Please enter a search term!"
            return render(request, 'search.html', {'msg': msg})
        else:
            printUtil.printSFDP2PDF(db, q)
            mypdf = 'dblpGraphs/static/output/coadb_coauthors_' + printUtil.pathEsc(u) + '.sfdp.pdf'
            with open(mypdf, 'r') as pdf:
                # response = HttpResponse(pdf.read(), mimetype='application/pdf')
                response = HttpResponse(content_type='application/pdf')
                response['Content-Disposition'] = 'inline;filename=%s.pdf' % ("Coauthors of coauthors of " + u)
            return response
