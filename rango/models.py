from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User)

    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to="profileImages", blank=True)

    def __unicode__(self):
        return self.user.username


class Category(models.Model):
    user = models.OneToOneField(User)

    category_title = models.CharField(max_length=35)

    def __unicode__(self):
        return self.category_title