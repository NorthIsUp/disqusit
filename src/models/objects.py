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

class DisqusitUser(Base):
	username = db.Column(db.String(30), primary_key = True) ##Usernames are db keys
	##TODO Add more things

	def __init__(self, username):
		self.username = username

	def __repr__(self):
		return "<User %r>" % (self.username)