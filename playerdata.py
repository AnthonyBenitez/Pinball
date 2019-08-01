from playermodels import PlayerModel


def save_profile(first, last, email, password, retypePassword, score, machine):
    p = get_user(first)
    if p:
        p.firstName = first
        p.lastName = last
        p.email = email
        p.password = password
        p.retypePassword = retypePassword
        p.score = 0
        p.machine = machine
        p.invalidated = False

    if not p:
        p = PlayerModel(
            firstName=first, lastName=last, email=email, password=password,
            retypePassword=retypePassword, score=0, machine=machine, invalidated=False)
    p.put()


def get_user(firstName):
    q = PlayerModel.query(PlayerModel.firstName == firstName)
    results = q.fetch(1)
    for profile in results:
        return profile
    return None


def load_user_profile(email):
    q = PlayerModel.query(PlayerModel.email == email)
    users = q.fetch(1)
    for profile in users:
        return profile
    return PlayerModel(firstName="", lastName="", email="", score=0, machine='', invalidated=False)


def ranking(top, machine):
    q = PlayerModel.query(PlayerModel.machine == machine).order(-PlayerModel.score)
    results = q.fetch(top)
    return results
