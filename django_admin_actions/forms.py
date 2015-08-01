# coding: utf-8
from __future__ import unicode_literals
from collections import OrderedDict

from django import forms
from django.utils.translation import ugettext_lazy as _


def make_form(BaseForm):
    class ActionModelForm(BaseForm):
        disable_preifx = 'disable__'

        _selected_action = forms.CharField(widget=forms.MultipleHiddenInput)

        def __init__(self, *args, **kwargs):
            super(ActionModelForm, self).__init__(*args, **kwargs)
            fields = OrderedDict()
            for fname, field in self.fields.items():
                fields[fname] = field
                if not fname.startswith('_'):
                    fields[self.make_disable_fname(fname)] = \
                        forms.BooleanField(label=_('disable'),
                                           required=False,
                                           initial=True)
            self.fields = fields

        def make_disable_fname(self, fname):
            return '{}{}'.format(self.disable_preifx, fname)

    return ActionModelForm
