#!/usr/bin/env python

import codenamer
import os, re, jinja2, webapp2

from google.appengine.ext import db

jinja_environment = jinja2.Environment(autoescape=True,
		loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__),
            'templates')))

EMAIL_RE  = re.compile(r'^[\S]+@[\S]+\.[\S]+$')
def valid_email(email):
    return not email or EMAIL_RE.match(email)

class Santa(db.Model):
    # Required at construction
    name = db.StringProperty(required=True)
    email = db.StringProperty(required=True)

    # optional
    message = db.TextProperty()
    choice = db.StringProperty()

    # Assigned at construction
    codename = db.StringProperty()

    # Assigned later
    assignment = db.StringProperty()
    photoURL = db.StringProperty

    def render(self):
        return self.name + ":" + self.codename

class BaseHandler(webapp2.RequestHandler):
    def render_str(self, template, **params):
        t = jinja_environment.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        r = self.render_str(template, **kw)
        self.response.out.write(r)

    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)


class WelcomeHandler(BaseHandler):
    template = "welcome.html"

    def get(self):
        pass

    def post(self):
        pass

class SignupHandler(BaseHandler):
    template = "signup.html"

    def get(self):
        santas = Santa.all()
        self.render(self.template, text='Howdy', santas=santas)

    def post(self):
        name = self.request.get('name')
        email = self.request.get('email')
        choice = self.request.get('choice')
        message = self.request.get('message')

        if name and email:
            codename = codenamer.generate_codename(name)

            santa = Santa(name=name, email=email, choice=choice,
                    message=message, codename=codename)

            santa.put()
            
            self.render("success.html", name=name, codename=codename)

app = webapp2.WSGIApplication([
    ('/', WelcomeHandler),
    ('/apply', SignupHandler)], debug=True)
