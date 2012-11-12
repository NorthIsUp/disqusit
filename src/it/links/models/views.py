from django.db import models
from django.contrib.auth.models import User
from links.models.base import BaseModel


class View(BaseModel):
    '''
    views are like subreddits
    '''
    viewer = models.TextField()
    creator = models.ForeignKey(User)
    owner = models.ForeignKey(User)
    moderators = models.ManyToManyField(User)
