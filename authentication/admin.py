# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from authentication.models import Person
# Register your models here.
from django.conf import settings
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from django.db.models import Q

# Register your models here.

#### customized class to authenticate the user. it'll check against your mobile, email and username if exists or not
class SettingsBackend(object):
	print("inside admin filsse")
	def authenticate(self, request, username=None, password=None):
		print('inside authenticate')
		try:
			#######for Admin pannel value will be come in username and for APIs value will be come in email##
			try:
				user = User.objects.get(Q(username=email)| Q(email=email) | Q(mobile=email))
			except:
				user = User.objects.get(Q(username=username) | Q(mobile=username) | Q(email=username))
			if user.check_password(password):
				return user
			else:
				pass
		except User.DoesNotExist:
			User().set_password(password)

	def get_user(self, user_id):
		try:
			return User.objects.get(pk=user_id)
		except User.DoesNotExist:
			return None


admin.site.register(Person)