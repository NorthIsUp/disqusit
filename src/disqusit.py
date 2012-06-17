from flask import Flask
app = Flask(__name__)

from flask import session
from flask import redirect
from flask import url_for
from flask import escape
from flask import request

import functools
import simplejson
import urllib
import urllib2
from functools import wraps

import wtforms
from wtforms import Form, BooleanField, TextField, PasswordField, validators

from flask import render_template

from disqusapi import InvalidAccessToken
from disqusapi import DisqusAPI

from flask.ext.sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/disqusit.db'
db = SQLAlchemy(app)


################################################################################

## MODELS ##


class Link(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(500))
    title = db.Column(db.String(500))
    shortname = db.Column(db.String(100))		##TODO Are these max lengths ok?
    disqus_identifier = db.Column(db.String(100))
    disqus_votes = db.Column(db.Integer)
    disqusit_votes = db.Column(db.Integer)

    def __init__(self, url=None, shortname=None, disqus_id=None,
                 disqus_votes=0, disqusit_votes=0):
        self.url = url
        self.shortname = url
        self.disqus_identifier = disqus_id
        self.disqus_votes = disqus_votes
        self.disqusit_votes = disqusit_votes

    def __repr__(self):
        return "<Link %r>" % (self.url)

class DisqusitUser(db.Model):
    username = db.Column(db.String(30), primary_key = True) ##Usernames are db keys
    ##TODO Add more things

    def __init__(self, username):
        self.username = username

    def __repr__(self):
        return "<User %r>" % (self.username)

################################################################################



class SubmitLinkForm(Form):
        link = TextField('Link', [validators.Length(min=4, max=25)])
        title = TextField('Title', [validators.Length(min=4, max=25)])


@app.route("/news")
def news():
    return render_template('base.html', form=SubmitLinkForm(request.form))


@app.route('/news', methods=['POST'])
def submitLink():
    form = SubmitLinkForm(request.form)
    if form.validate():

        # DO SCRAPING HERE #
        shortname = 0
        disqus_identifier = 0
        disqus_votes = 0
        disqusit_votes = 0

        link = Link(form.link, form.title,  shortname, disqus_identifier, disqus_votes, disqusit_votes)
        db.session.add(link)

## AUTH STUFF (DO NOT CHANGE)

## RUN IT

if __name__ == "__main__":
    app.config["DEBUG"] = True
    app.run()


