# -*- coding: utf-8 -*-
import os
from django.db import models
from django_countries import CountryField
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django import forms
from django.forms.extras.widgets import SelectDateWidget
from django.utils.html import strip_tags
import HTMLParser

# Create your models here.

class Company(models.Model):
	name = models.CharField(max_length=100)

	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name = 'Company'
		verbose_name_plural = 'Compnies'



class Property(models.Model):
	STATUS = (
    ('pending', 'Pending'),
    ('active', 'Active'),
    ('canceled', 'Cancelled'),
    ('hidden', 'Hidden'),
	)
	user = models.ForeignKey(User)
	company = models.ForeignKey(Company)
	name = models.CharField(max_length=200, verbose_name="Property Name")
	description = HTMLField()
	address1 = models.CharField(max_length=50)
	address2 = models.CharField(max_length=50)
	city = models.CharField(max_length=50)
	state = models.CharField(max_length=50)
	country = CountryField()
	zipcode = models.IntegerField(max_length=5)
	status =   models.CharField(max_length=20, choices=STATUS, default="pending")
	created = models.DateTimeField(default=datetime.now(),blank=True)
	updated = models.DateTimeField(default=datetime.now(),blank=True)


	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name = 'Property'
		verbose_name_plural = 'Properties'

class Property_Tax_Condition(models.Model):

	def file_get_contents(filename):
		path = os.path.dirname(os.path.abspath( __file__ ))
		try:
			with open(path+'/'+filename) as f:
				return f.read()
		except IOError as e:
			return "please set property terms and condition " + e

	property = models.ForeignKey(Property)
	terms = HTMLField(default=file_get_contents("terms_condition_default.txt"))
	created = models.DateTimeField(default=datetime.now(),blank=True)
	updated = models.DateTimeField(default=datetime.now(),blank=True)

	def __unicode__(self):
		return HTMLParser.HTMLParser().unescape(strip_tags(self.terms)[:75].rsplit(' ', 1)[0] + (strip_tags(self.terms)[:500] and ' . . .'))

	class Meta:
		verbose_name = 'Terms'
		verbose_name_plural = 'Terms'

