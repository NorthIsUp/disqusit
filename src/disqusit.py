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

from disqusapi import InvalidAccessToken
from disqusapi import DisqusAPI


from flask.ext.sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/disqusit.db'
db = SQLAlchemy(app)

## TODO: make this read from a file
#public_key = "PUT YOUR KEY HERE"
#secret_key = "PUT YOUR KEY HERE"

#app.secret_key = "this is my salt"

#disqus = DisqusAPI(secret_key, public_key)


################################################################################
## UTILS


#class User(object):
#    """User object based on disqus auth token"""
#    def __init__(self, username, user_id, access_token, expires_in, token_type, refresh_token):
#        super(User, self).__init__()
#        self.username = username
#        self.user_id = user_id
#        self.access_token = access_token
#        self.expires_in = expires_in
#        self.token_type = token_type
#        self.refresh_token = refresh_token

#    def __repr__(self):
#        return "<{username}:{access_token}>".format(**self.__dict__)


#def current_user():
#    cu = None
#    if 'auth' in session:
#        auth = session['auth']
#        cu = User(**auth)
#    return cu


################################################################################
## APP


@app.route("/news")
def news():
    return "the news"


#@app.route("/")
##def hello():
##    cu = current_user()
##    if cu:
##        return 'Logged in as %s' % escape(session['username'])
##    else:
##        return redirect('/oauth/authorize/')

################################################################################
## AUTH STUFF (DO NOT CHANGE)

class Logout(Exception):
    pass


def api_call(func, **kwargs):
    try:
        if 'auth' in session:
            result = func(access_token=session['auth']['access_token'], **kwargs)
        else:
            result = func(**kwargs)
    except InvalidAccessToken:
        raise Logout
    return result


@app.errorhandler(Logout)
def logout_handler(error):
    try:
        del session['auth']
    except KeyError:
        pass
    return redirect(url_for('oauth_authorize'))


def login_required(func):
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        if 'auth' not in session:
            return redirect(url_for('oauth_authorize'))
        return func(*args, **kwargs)
    return wrapped


@app.route('/oauth/authorize/')
def oauth_authorize():
    return redirect('https://disqus.com/api/oauth/2.0/authorize/?%s' % (urllib.urlencode({
        'client_id': disqus.public_key,
        'scope': 'read,write',
        'response_type': 'code',
        'redirect_uri': url_for('oauth_callback', _external=True),
    }),))


@app.route('/oauth/callback/')
def oauth_callback():
    code = request.args.get('code')
    error = request.args.get('error')
    if error or not code:
        # TODO: show error
        return redirect('/')

    req = urllib2.Request('https://disqus.com/api/oauth/2.0/access_token/', urllib.urlencode({
        'grant_type': 'authorization_code',
        'client_id': disqus.public_key,
        'client_secret': disqus.secret_key,
        'redirect_uri': url_for('oauth_callback', _external=True),
        'code': code,
    }))

    resp = urllib2.urlopen(req).read()

    data = simplejson.loads(resp)

    session['auth'] = data
    session['username'] = data['username']
    session.permanent = True

    return redirect('/')

################################################################################

## MODELS ##


class Link(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(500))
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

## RUN IT

if __name__ == "__main__":
    app.config["DEBUG"] = True
    app.run()


