# coding: utf-8
from __future__ import unicode_literals

from django.contrib import admin
from django_admin_actions import ActionForm, ActionModelForm

from .models import BlogPost

from django import forms


class SimpleForm(forms.Form):
    hello = forms.CharField()


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title',)
    fields = ('title', 'lead', 'body',)
    actions = (ActionModelForm.as_action(short_description='Hello'),)

admin.site.register(BlogPost, BlogPostAdmin)
