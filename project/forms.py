#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from .models import Project as Model


class ProjectForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Model