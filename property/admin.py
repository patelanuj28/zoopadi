# -*- coding: utf-8 -*-
from django.contrib import admin
from property.models import Company, Property, Property_Tax_Condition
from django.contrib.auth.models import User
from django.conf.urls import patterns, url
from django.http import HttpResponse, HttpResponseRedirect, HttpResponse, Http404
from django.template import RequestContext, loader
from django.shortcuts import render, get_object_or_404, render_to_response
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage
from django.core import serializers
from django.utils.html import strip_tags


class Property_Tax_Condition_Admin(admin.ModelAdmin):
	fieldsets = [
			(None, {'fields': ['property']}),
			('Property Information', {'fields': [ 'terms']}),
			]

	list_display = ('property', 'html_terms')
	search_fields = ['terms',]
	#list_editable = ( 'terms', )

	def html_terms(self, obj):
		return obj.terms[:500].rsplit(' ', 1)[0] + (strip_tags(obj.terms)[:500] and ' <font color="blue"><strong>. . . continue . . .</strong></font>')

	html_terms.allow_tags = True

Property_Tax_Condition_Admin.allow_tags = True


class Property_Admin(admin.ModelAdmin):
	fieldsets = [
			(None, {'fields': ['name', 'company']}),
			('Property Information', {'fields': [ 'description', 'address1', 'address2', 'city', 'state', 'country', 'zipcode', 'status']}),
			]

	list_display = ('name', 'company', 'user', 'address1', 'address2', 'city', 'state', 'country', 'zipcode', 'status')
	list_filter = ['created']
	search_fields = ['name','address1', 'address2', 'city', 'state', 'country', 'zipcode', 'status']
	list_editable = ( 'status', )
	date_hierarchy = 'created'
	extra_context = {'show_save_and_add_another': False,'show_save_and_continue': False}


	def make_active(modeladmin, request, queryset):
	    queryset.update(status='active')
	make_active.short_description = "Mark selected property as Active"

	def make_pending(modeladmin, request, queryset):
	    queryset.update(status='pending')
	make_pending.short_description = "Mark selected property as Pending"

	def make_hidden(modeladmin, request, queryset):
	    queryset.update(status='hidden')
	make_hidden.short_description = "Mark selected property as Hidden"

	def make_cancelled(modeladmin, request, queryset):
	    queryset.update(status='canceled')
	make_cancelled.short_description = "Mark selected property as Cancelled"

	actions = [make_active, make_pending, make_hidden, make_cancelled]


	def get_actions(self, request):
		actions = super(Property_Admin, self).get_actions(request)

		if request.user.username.upper() != "PATELANUJ28":
			if 'delete_selected' in actions:
				del actions['delete_selected']
		return actions

	def save_model(self, request, obj, form, change):
		obj.user = request.user
		if obj.name:
			obj.save()

	


class Company_Admin(admin.ModelAdmin):
	pass


Property_Admin.list_per_page =10

Company_Admin.list_per_page =10

admin.site.register(Company, Company_Admin)
admin.site.register(Property, Property_Admin)
admin.site.register(Property_Tax_Condition, Property_Tax_Condition_Admin)


