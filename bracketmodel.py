from google.appengine.ext import ndb


class BracketModel(ndb.Model):
    name = ndb.StringProperty()
    numTeams = ndb.IntegerProperty()
    teams = ndb.StringProperty()
    maxScore = ndb.IntegerProperty()
    numRounds = ndb.IntegerProperty()
    totalNumTeams = ndb.IntegerProperty()
    totalTeams = ndb.IntegerProperty()
    lineup = ndb.StringProperty()
    count = ndb.IntegerProperty()
    rounds = ndb.StringProperty(repeated=True)
