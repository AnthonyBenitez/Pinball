import playermodels.py
from google.appengine.ext import ndb

score1 = 0
score2 = 0
score3 = 0
name1 = ""
name2 = ""
name3 = ""


class ranking():
    q = PlayerModel.query(PlayerModel.name == name)
    results = q.fetch(1)
    for profile in results:
        return profile
    return None
