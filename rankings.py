from playermodels import PlayerModel
# from google.appengine.ext import ndb

score1 = 0
score2 = 0
score3 = 0
name1 = ""
name2 = ""
name3 = ""


def ranking():
    q = PlayerModel.query(PlayerModel.firstName == firstName)
    results = q.fetch(1)
    for profile in results:
        return profile
    return None
