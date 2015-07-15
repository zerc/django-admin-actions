# coding: utf-8
from django.views.generic.base import TemplateView


class IndexPage(TemplateView):
    template_name = 'index.html'
