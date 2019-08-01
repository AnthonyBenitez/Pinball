from google.appengine.ext import ndb


class PlayerModel(ndb.Model):
    firstName = ndb.StringProperty()
    lastName = ndb.StringProperty()
    email = ndb.StringProperty()
    score = ndb.IntegerProperty()
    machine = ndb.StringProperty()
    invalidated = ndb.BooleanProperty()
