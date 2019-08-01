from playermodels import PlayerModel
# from google.appengine.ext import ndb


def ranking():
    q = PlayerModel.query(PlayerModel.firstName == firstName)
    results = q.fetch(1)
    for profile in results:
        return profile
    return None
