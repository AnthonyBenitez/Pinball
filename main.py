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
            playerdata.save_profile(
                firstName, lastName, email, password, score, machine)
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
            if error_text:
                values['errormsg'] = error_text
            else:
                playerdata.save_profile(
                    email, firstName, lastName, email, password, score, machine)
                values['successmsg'] = 'Everything worked out fine.'
            render_template(self, 'pinballhomepage.html', values)


class FakeDataHandler(webapp2.RequestHandler):
    def get(self):
        p1 = playermodels.PlayerModel(firstName="Anthony", lastName="Benitez",
         email="tony20882@gmail.com", score=10000000, machine = 'terminator 3')
        p1.put()
        p2 = playermodels.PlayerModel(firstName="Langston", lastName="Luck",
         email="langstonluck@gmail.com", score=777777, machine = 'terminator 3')
        p2.put()
        p3 = playermodels.PlayerModel(firstName="Benithan", lastName="Pinball",
         email="pinballben@gmail.com", score=999999999, machine = 'terminator 3')
        p3.put()
        p3 = playermodels.PlayerModel(firstName="John", lastName="Homie",
         email="johnny@gmail.com", score=888888888, machine = 'terminator 3')
        p3.put()
        p4 = playermodels.PlayerModel(firstName="Dude", lastName="Homie",
         email="dude@gmail.com", score=75, machine = 'game of thrones')
        p4.put()
        self.response.out.write('successfully seeded data!')


app = webapp2.WSGIApplication([
    ('/p/(.*)', CreateUserHandler),
    ('/termleaderboard', TermLeaderboardHandler),
    ('/adamleaderboard', adamLeaderboardHandler),
    ('/gotleaderboard', gotLeaderboardHandler),
    ('/fake', FakeDataHandler),
    ('.*', MainHandler)
])
