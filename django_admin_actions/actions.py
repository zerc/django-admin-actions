# coding: utf-8
from __future__ import unicode_literals
from collections import OrderedDict

from django.views.generic import View, FormView
from django.utils.decorators import classonlymethod
from django.views.generic.edit import BaseUpdateView
from django.utils.translation import ugettext_lazy as _

from .forms import make_form


class Action(View):
    """ Generic view based action.
    """
    model_admin = None
    queryset = None
    short_description = None

    @classonlymethod
    def as_action(cls, **initkwargs):
        def wrapper(model_admin, request, queryset):
            view = cls.as_view(model_admin=model_admin, queryset=queryset,
                               **initkwargs)
            return view(request)

        wrapper.short_description = \
            initkwargs.get('short_description', cls.short_description)

        return wrapper

    def dispatch(self, request, *args, **kwargs):
        method = request.method.lower()

        if method not in self.http_method_names:
            return self.http_method_not_allowed(request, *args, **kwargs)

        if method == 'post' and 'apply' not in request.POST:
            method = 'get'

        handler = getattr(self, method, self.http_method_not_allowed)

        return handler(request, *args, **kwargs)


class ActionForm(Action, FormView):
    """ Form based action.
    """
    template_name = 'django_admin_actions/action_form.html'

    def get_form(self, *args, **kwargs):
        assert self.form_class is not None, 'Missed required `form_class` arg'
        return make_form(super(ActionForm, self).get_form(*args, **kwargs))


class ActionModelForm(ActionForm):
    """ Action for mass changing fields values
    """
    def get_form(self, *args, **kwargs):
        return make_form(self.model_admin.get_form(self.request))
