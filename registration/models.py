from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):
    name = models.CharField(max_length=255)
    users = models.ManyToManyField(User)
    active = models.BooleanField(default=True)