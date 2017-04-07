from dblpGraphs import statsUtil

from parser.pySaxParser import ch as db


class Stats:
    def __init__(self):
        self.topAuthors = statsUtil.topAuthors(db, 15)
        self.topCoAuthors = statsUtil.topCoAuthors(db, 15)
        self.mean = statsUtil.publicationsMean(db)
        self.var = statsUtil.publicationsVar(db)
        self.median = statsUtil.publicationsMedian(db)
        self.mode = statsUtil.publicationsMode(db)
        coa_stats = statsUtil.coAuthorStats(db)
        self.coaMean = coa_stats[0]
        self.coaVar = coa_stats[1]
        self.coaMedian = coa_stats[2]
        self.coaMode = coa_stats[3]
        self.publications = statsUtil.publicationsDistribution(db)


