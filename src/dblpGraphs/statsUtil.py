import time
import urllib.request, urllib.parse, urllib.error
from operator import itemgetter

import numpy


# Some statistics of the global database
def publicationsMean(database):
    return numpy.mean(list(database.authorsPubdb.values()))


def publicationsMedian(database):
    return numpy.median(list(database.authorsPubdb.values()))


def publicationsVar(database):
    return numpy.var(list(database.authorsPubdb.values()))


def publicationsMode(database):
    return numpy.argmax(numpy.bincount(list(database.authorsPubdb.values())))


def coAuthorStats(database):
    values = []
    for coacount in list(database.coauthorsDB.values()):
        if not coacount:
            values.append(0)
        else:
            values.append(len(coacount))
    return [numpy.mean(values), numpy.var(values), numpy.median(values), numpy.argmax(numpy.bincount(values))]


# Aggregates the percentages of the publications in an array of tuples
def publicationsDistribution(database):
    sumPubs = 0
    for (k, v) in list(database.db.items()):
        sumPubs += v
    distribution = sorted(database.db, key=database.db.get, reverse=True)
    pDistribution = []
    for k in distribution:
        pDistribution.append((k, "%.4f" % ((database.db[k] / (sumPubs + 0.0)) * 100)))

    return pDistribution


# Aggregates the top n authors, by their publication count
def topAuthors(database, n):
    authors = []
    names = sorted(database.authorsPubdb, key=database.authorsPubdb.get, reverse=True)[:n]
    for name in names:
        authors.append((urllib.parse.unquote(name), database.authorsPubdb[name]))
    return authors


# Aggregates the top n authors, by their coauthors count
def topCoAuthors(database, n):
    sorted_coauthors = sorted(database.coauthorsDB, key=lambda k: len(database.coauthorsDB[k]), reverse=True)
    return [(urllib.parse.unquote(name), len(database.coauthorsDB[name])) for name in sorted_coauthors]


# An auxiliary method for printing
def printPublicationDistr(database):
    sumPubs = 0
    for (k, v) in list(database.db.items()):
        sumPubs += v
    print("The distribution of publications is the following:")
    for (k, v) in list(database.db.items()):
        p = ((v / (sumPubs + 0.0)) * 100)
        print(k + ': ' + str(v) + ' (%.4f percent)' % p)
