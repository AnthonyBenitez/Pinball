from playermodels import PlayerModel


def save_profile(first, last, email, password, retypePassword):
    p = get_user(first)
    if p:
        p.firstName = first
        p.lastName = last
        p.email = email
        p.password = password
        p.retypePassword = retypePassword
        p.score = 0

    if not p:
        p = PlayerModel(
            firstName=first, lastName=last, email=email, password=password, retypePassword=retypePassword, score=0)
    p.put()


def get_user(name):
    q = PlayerModel.query(PlayerModel.name == name)
    results = q.fetch(1)
    for profile in results:
        return profile
    return None


def load_user_profile(email):
    q = PlayerModel.query(PlayerModel.email == email)
    users = q.fetch(1)
    for profile in users:
        return profile
    return


def ranking(top):
    q = PlayerModel.query().order(-PlayerModel.score)
    results = q.fetch(top)
    return results
