from django.contrib.auth.models import User
from django.db import models
from links.models.base import BaseModel


class Link(BaseModel):
    disqus_identifier = models.TextField()
    disqus_url = models.TextField()
    disqus_shortname = models.CharField(max_size=256)
    submitter = models.ForeignKey(User)
    tags = models.ManyToManyField('links.models.Tag')
    url = models.TextField()
    views = models.ManyToManyField('links.models.View')

    #add votes
    #link votes to disqus threadvotes
