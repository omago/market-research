#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from django.forms.models import BaseModelFormSet

from .models import Note as Model


class NoteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(NoteForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Model


class BaseNoteFormSet(BaseModelFormSet):
    def __init__(self, *args, **kwargs):
        super(BaseNoteFormSet, self).__init__(*args, **kwargs)


class NoteFormsetForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(NoteFormsetForm, self).__init__(*args, **kwargs)
        self.fields["note"].widget = forms.TextInput()

    class Meta:
        model = Model
        fields = ("note_type",
                  "note")

    def save(self, commit=True, created_by=None, research=None, *args, **kwargs):
        note = super(NoteFormsetForm, self).save(commit=False)

        if "note" in self.cleaned_data:

            note.research = research

            if commit:
                note.save()

            return note