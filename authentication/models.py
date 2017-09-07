# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Person(models.Model):
	user= models.ForeignKey(User, blank= True)
	is_active= models.BooleanField(default= True)

	def __str__(self):
		return self.user.first_name	