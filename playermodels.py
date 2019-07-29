from google.appengine.ext import ndb


class PlayerModel(ndb.Model):
    firstName = ndb.StringProperty()
    lastName = ndb.StringProperty()
    email = ndb.StringProperty()
    password = ndb.StringProperty()
    retypePassword = ndb.StringProperty()
    score = ndb.IntegerProperty()
