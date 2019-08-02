import os
import webapp2
import playermodels
import playerdata
# import bracketMain
# import bracket
# from bracketmodel import BracketModel

from google.appengine.api import users
from google.appengine.ext.webapp import template


# bracket.run()

def render_template(handler, file_name, template_values):
    path = os.path.join(os.path.dirname(__file__), 'templates/', file_name)
    handler.response.out.write(template.render(path, template_values))


def get_user_email():
    user = users.get_current_user()
    if user:
        nickname = user.nickname()
        logout_url = users.create_logout_url('/')
        # greeting = 'Welcome {}! Are you ready to win the pin? (<a href = "{}"> sign out </a>)'.format(nickname, logout_url)
        return "example@google.com"
        #return user.email()
    else:
        login_url = users.create_login_url('/')
        # greeting = 'Welcome! <a href="{}">Sign in</a>'.format(login_url)
        return "User does not exist"


def get_template_parameters():
    values = {}
    if get_user_email():
        values['logout_url'] = users.create_logout_url('/')
    else:
        values['login_url'] = users.create_login_url('/')
    return values


class MainHandler(webapp2.RequestHandler):
    def get(self):
        values = get_template_parameters()
        if get_user_email():
            profile = playerdata.load_user_profile(get_user_email())
            # values['firstName'] = profile.firstName
        render_template(self, 'pinballhomepage.html', values)


class TermLeaderboardHandler(webapp2.RequestHandler):
    def get(self):
        values = get_template_parameters()
        if get_user_email():
            profile = playerdata.load_user_profile(get_user_email())
            values['firstName'] = profile.firstName
            values['ranking'] = playerdata.ranking(10, 'terminator 3')
            values['score'] = profile.score
            values['machine'] = profile.machine
            values['invalidated'] = profile.invalidated
        render_template(self, 'terminatorLeaderboard.html', values)


class gotLeaderboardHandler(webapp2.RequestHandler):
    def get(self):
        values = get_template_parameters()
        if get_user_email():
            profile = playerdata.load_user_profile(get_user_email())
            values['firstName'] = profile.firstName
            values['ranking'] = playerdata.ranking(10, 'game of thrones')
            values['score'] = profile.score
            values['machine'] = profile.machine
            values['invalidated'] = profile.invalidated
        render_template(self, 'gotLeaderboard.html', values)


class adamLeaderboardHandler(webapp2.RequestHandler):
    def get(self):
        values = get_template_parameters()
        if get_user_email():
            profile = playerdata.load_user_profile(get_user_email())
            values['firstName'] = profile.firstName
            values['ranking'] = playerdata.ranking(10, 'adams family')
            values['score'] = profile.score
            values['machine'] = profile.machine
            values['invalidated'] = profile.invalidated
        render_template(self, 'adamsLeaderboard.html', values)


class CreateUserHandler(webapp2.RequestHandler):
    def post(self):
        email = get_user_email()
        if not email:
            self.redirect('/')
        else:
            error_text = ''
            firstName = self.request.get('firstName')
            lastName = self.request.get('lastName')
            email = self.request.get('email')
            password = self.request.get('password')
            score = self.request.get('score')
            machine = self.request.get('machine')
            invalidated = self.request.get('invalidated')
            playerdata.save_profile(
                firstName, lastName, email, password, score, machine, invalidated)
            self.redirect('/profile-edit')

            if len(firstName) < 2:
                error_text += 'Name should be at least 2 characters.\n'
            if len(firstName) > 50:
                error_text += 'Name should be no more than 50 characters.\n'
            if len(firstName.split()) > 1:
                error_text += 'Name should not have whitespace.\n'
            values = get_template_parameters()
            values['firstName'] = firstName
            values['lastName'] = lastName
            values['email'] = email
            values['password'] = password
            values['score'] = score
            values['machine'] = machine
            values['invalidated'] = invalidated
            if error_text:
                values['errormsg'] = error_text
            else:
                playerdata.save_profile(
                    email, firstName, lastName, email, password, score, machine, invalidated)
                values['successmsg'] = 'Everything worked out fine.'
            render_template(self, 'pinballhomepage.html', values)


class FakeDataHandler(webapp2.RequestHandler):
    def get(self):
        p1 = playermodels.PlayerModel(firstName="Juliette", lastName="Koval",
         email="jkoval@gmail.com", score= 12356800, machine='terminator 3', invalidated=False)
        p1.put()
        p2 = playermodels.PlayerModel(firstName="Langston", lastName="Luck",
         email="langstonluck@gmail.com", score=74368600, machine='terminator 3', invalidated=False)
        p2.put()
        p3 = playermodels.PlayerModel(firstName="Full Send", lastName="Mercedes",
         email="pinballcedes@gmail.com", score=147683400, machine='terminator 3', invalidated=False)
        p3.put()
        p4 = playermodels.PlayerModel(firstName="Blonde John", lastName="Homie",
         email="homiejohn@gmail.com", score=65234900, machine='terminator 3', invalidated=False)
        p4.put()
        p5 = playermodels.PlayerModel(firstName="Isabel", lastName="Mitre",
         email="isabelmitre@gmail.com", score=59382100, machine='terminator 3', invalidated=False)
        p5.put()
        p6 = playermodels.PlayerModel(firstName="Anthony", lastName="Benitez",
         email="tony20882@gmail.com", score=75542700, machine='game of thrones', invalidated=False)
        p6.put()
        p7 = playermodels.PlayerModel(firstName="Langston", lastName="Luck",
         email="langstonluck@gmail.com", score=78294900, machine='game of thrones', invalidated=False)
        p7.put()
        p8 = playermodels.PlayerModel(firstName="Tim", lastName="James",
         email="timjames@gmail.com", score=83592700, machine='game of thrones', invalidated=False)
        p8.put()
        p9 = playermodels.PlayerModel(firstName="Steve", lastName="Pinball",
         email="stevenpinball@gmail.com", score=50234780, machine='game of thrones', invalidated=False)
        p9.put()
        p10 = playermodels.PlayerModel(firstName="Francisco", lastName="Pinball",
         email="Francisco@gmail.com", score=63673100, machine='game of thrones', invalidated=False)
        p10.put()
        p11 = playermodels.PlayerModel(firstName="Anthony", lastName="Benitez",
         email="tony20882@gmail.com", score=10000000, machine='addams', invalidated=False)
        p11.put()
        p12 = playermodels.PlayerModel(firstName="Langston", lastName="Luck",
         email="langstonluck@gmail.com", score=777777, machine='terminator 3', invalidated=False)
        p12.put()
        p13 = playermodels.PlayerModel(firstName="Jon", lastName="Pinball",
         email="pinballben@gmail.com", score=999999999, machine='terminator 3', invalidated=False)
        p13.put()
        p14 = playermodels.PlayerModel(firstName="Steven", lastName="Homie",
         email="johnny@gmail.com", score=888888888, machine='terminator 3', invalidated=False)
        p14.put()
        p15 = playermodels.PlayerModel(firstName="Stephen", lastName="Homie",
         email="dude@gmail.com", score=75, machine='game of thrones', invalidated=False)
        p15.put()
        self.response.out.write('Successfully seeded data!')


class InvalidationHandler(webapp2.RequestHandler):
    def get(self):
        values = get_template_parameters()
        if get_user_email():
            profile = playerdata.load_user_profile(get_user_email())
            values['firstName'] = profile.firstName
            values['ranking'] = playerdata.ranking(10, 'game of thrones')
            values['score'] = profile.score
            values['machine'] = profile.machine
            values['invalidated'] = profile.invalidated
        render_template(self, 'invalidatescore.html', values)
        # self.response.out.write('Suggestion has been sent!')

app = webapp2.WSGIApplication([
    ('/p/(.*)', CreateUserHandler),
    ('/termleaderboard', TermLeaderboardHandler),
    ('/adamleaderboard', adamLeaderboardHandler),
    ('/gotleaderboard', gotLeaderboardHandler),
    ('/fake', FakeDataHandler),
    ('/invalidate', InvalidationHandler),
    ('.*', MainHandler)
])
