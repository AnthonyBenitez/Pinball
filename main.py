import os
import webapp2
import playermodels
import playerdata

from google.appengine.ext import users
from google.appengine.ext.webapp import template


def render_template(handler, file_name, template_values):
    path = os.path.join(os.path.dirname(__file__), 'templates/', file_name)
    handler.response.out.write(template.render(path, template_values))


def get_user_email():
    user = users.get_current_user()
    if user:
        return user.email()
    else:
        return None


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
            values['name'] = profile.name
        render_template(self, 'mainpage.html', values)


class LeaderboardHandler(webapp2.RequestHandler):
    def get(self):
        values = get_template_parameters()
        if get_user_email():
            profile = playerdata.load_user_profile(get_user_email())
            values['firstname'] = profile.firstName
            values['score'] = profile.score
        render_template(self, "leaderboard.html", values)


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
            playerdata.save_profile(
                firstName, lastName, email, password, score)
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
            if error_text:
               values['errormsg'] = error_text
            else:
                playerdata.save_profile(
                    email, firstName, lastName, email, password, score)
                values['successmsg'] = 'Everything worked out fine.'
            render_template(self, 'profile-edit.html', values)


app = webapp2.WSGIApplication(
    ('/sp', ),
    # ('.*', LeaderboardHandler)
)