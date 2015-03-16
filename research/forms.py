#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from .models import Research as Model


class ResearchForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ResearchForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Model