import os
import time
import urllib.request, urllib.parse, urllib.error


# Create a level-1 coauthors graph in the PNG format
def printSFDPa(database, author):
    startTime = time.time()
    sfdpFile = 'graph ' + dotFileEsc(author) + ' {\noverlap = false;\nsplines = spline;\n'

    relAuthors = set()
    relAuthors.add(author)
    for coAuthor in database.coauthorsDB[author]:
        relAuthors.add(coAuthor)

    for relAuthor in relAuthors:
        for coAuthor in database.coauthorsDB[relAuthor]:
            if coAuthor in relAuthors:
                sfdpFile += dotFileEsc(relAuthor) + ' -- ' + dotFileEsc(coAuthor) + '\n'

    sfdpFile += '}'
    sfdpFileName = outputPath("coadb_connected_", urllib.parse.unquote(author))

    f = open(sfdpFileName, 'wb')
    f.write(urllib.parse.unquote(sfdpFile))
    f.close()
    os.system('sfdp ' + sfdpFileName + ' -Gconcentrate=true -Tpng -o' + sfdpFileName + '.png')
    endTime = (time.time() - startTime)
    print("Created a connected PNG coauthor graph of '" + author + "' after %d m %d s!" % (endTime / 60, endTime % 60))


# Create a level-1 coauthors graph in the PDF format
def printSFDPaPDF(database, author):
    startTime = time.time()
    sfdpFile = 'graph ' + dotFileEsc(author) + ' {\noverlap = false;\nsplines = spline;\n'

    relAuthors = set()
    relAuthors.add(author)
    for coAuthor in database.coauthorsDB[author]:
        relAuthors.add(coAuthor)

    for relAuthor in relAuthors:
        for coAuthor in database.coauthorsDB[relAuthor]:
            if coAuthor in relAuthors:
                sfdpFile += dotFileEsc(relAuthor) + ' -- ' + dotFileEsc(coAuthor) + '\n'

    sfdpFile += '}'
    sfdpFileName = outputPath("coadb_connected_", urllib.parse.unquote(author))

    f = open(sfdpFileName, 'wb')
    f.write(urllib.parse.unquote(sfdpFile))
    f.close()
    os.system('sfdp ' + sfdpFileName + ' -Gconcentrate=true -Tpdf -o' + sfdpFileName + '.pdf')
    endTime = (time.time() - startTime)
    print("Created a connected PNG coauthor graph of '" + author + "' after %d m %d s!" % (endTime / 60, endTime % 60))


# A prototype method for weighted graphs
def printSFDPaWeigths(database, author):
    startTime = time.time()
    sfdpFile = 'graph ' + dotFileEsc(author) + ' {\noverlap = false;\nsplines = spline;\n'

    relAuthors = set()
    relAuthors.add(author)
    for coAuthor in database.coauthorsDB[author]:
        relAuthors.add(coAuthor)

    for relAuthor in relAuthors:
        for coAuthor in database.coauthorsDB[relAuthor]:
            if coAuthor in relAuthors:
                sfdpFile += dotFileEsc(relAuthor) + ' -- ' + dotFileEsc(coAuthor) + ' [label=\"' + str(
                    database.coauthorsDB[relAuthor][coAuthor]) + '\"];\n'

    sfdpFile += '}'
    sfdpFileName = './output/coadbWeigths' + pathEsc(author) + '.sfdp'

    f = open(sfdpFileName, 'wb')
    f.write(sfdpFile.encode('utf8'))
    f.close()
    os.system('sfdp ' + sfdpFileName + ' -Tpdf -o' + sfdpFileName + '.pdf')
    endTime = (time.time() - startTime)
    print("Created a weigthed and connected PDF coauthor graph of '" + author + "' after %d m %d s!" % (
    endTime / 60, endTime % 60))


# Create a level-2 coauthors graph in the PDF format
def printSFDP2PDF(database, author):
    startTime = time.time()
    sfdpFile = 'graph ' + dotFileEsc(author) + ' {\noverlap = false;\nsplines = curved;\n'
    line = ''
    for coAuthor in database.coauthorsDB[author]:
        line += dotFileEsc(author) + ' --'
        line += ' ' + dotFileEsc(coAuthor) + '\n'
        for coAuthor2 in database.coauthorsDB[coAuthor]:
            oline = dotFileEsc(coAuthor) + ' --'
            oline += ' ' + dotFileEsc(coAuthor2) + '\n'
            sfdpFile += oline

    sfdpFile += line
    sfdpFile += '}'
    sfdpFileName = outputPath("coadb_coauthors_", urllib.parse.unquote(author))

    f = open(sfdpFileName, 'wb')
    f.write(urllib.parse.unquote(sfdpFile))
    f.close()
    os.system('sfdp ' + sfdpFileName + ' -Gconcentrate=true -Tpdf -o' + sfdpFileName + '.pdf')
    endTime = (time.time() - startTime)
    print("Created PDF coauthor of coauthors graph of '" + author + "' after %d m %d s!" % (endTime / 60, endTime % 60))


# Some auxiliary methods

def dotFileEsc(string):
    return '\"' + string + '\"'


def pathEsc(string):
    return string.replace(' ', '_').replace('.', '')


# Define the output path
def outputPath(mytype, author):
    return 'dblpGraphs/static/output/' + mytype + pathEsc(author) + '.sfdp'
