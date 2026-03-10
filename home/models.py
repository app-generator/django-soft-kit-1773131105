# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    username = models.CharField(max_length=255, null=True, blank=True)
    fullname = models.TextField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    passwordhash = models.CharField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Recipe(models.Model):

    #__Recipe_FIELDS__
    id = models.CharField(max_length=255, null=True, blank=True)
    name = models.TextField(max_length=255, null=True, blank=True)
    description = models.TextField(max_length=255, null=True, blank=True)
    summary = models.TextField(max_length=255, null=True, blank=True)
    ingredients = models.CharField(max_length=255, null=True, blank=True)
    instructions = models.CharField(max_length=255, null=True, blank=True)
    rating = models.IntegerField(null=True, blank=True)

    #__Recipe_FIELDS__END

    class Meta:
        verbose_name        = _("Recipe")
        verbose_name_plural = _("Recipe")



#__MODELS__END
