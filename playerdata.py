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
