#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from .models import NoteType as Model


class NoteTypeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(NoteTypeForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Model