from google.appengine.ext import ndb


class BracketModel(ndb.Model):
    numTeams = ndb.IntegerProperty()
    lastName = ndb.StringProperty()
    email = ndb.StringProperty()
    score = ndb.IntegerProperty()
    machine = ndb.StringProperty()
