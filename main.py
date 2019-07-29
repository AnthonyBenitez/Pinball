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




app = webapp2.WSGIApplication(
    ('/sp', ),
    ('.*', LeaderboardHandler)
)