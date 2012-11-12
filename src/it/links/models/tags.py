from django.db import models
from django.contrib.auth.models import User
from links.models.base import BaseModel


class Tag(BaseModel):
    name = models.TextField()
    creator = models.ForeignKey(User)
    owner = models.ForeignKey(User)
    moderators = models.ManyToManyField(User)
