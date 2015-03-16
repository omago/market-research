#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.forms.models import modelformset_factory

from core.helpers.view import get_list, get_details, get_form, get_delete
from .settings import context
from .models import Research as Model
from .forms import ResearchForm as ModelForm
from note.models import Note
from note.forms import BaseNoteFormSet, NoteFormsetForm

model = Model
model_form = ModelForm

@login_required
def list(request):
    return get_list(request, model, context, context["template_path"] + "/list.html")


@login_required
def form(request, pk=None):
    number_of_fields = 20
    NoteFormset = modelformset_factory(Note, form=NoteFormsetForm, formset=BaseNoteFormSet, extra=number_of_fields)

    if request.POST:
        if pk:
            entry = Model.objects.get(pk=pk)
            form = ModelForm(request.POST, instance=entry)
            note_formset = NoteFormset(request.POST)

        else:
            form = ModelForm(request.POST)
            note_formset = NoteFormset(request.POST)

        if form.is_valid() and note_formset.is_valid():
            research = form.save()
            for note_form in note_formset:
                note_form.save(research=research)

            return HttpResponseRedirect("/" + context["url_main"] + "/list/")
    else:
        if pk:
            form = ModelForm(instance=Model.objects.get(pk=pk))
            research_notes = Note.objects.filter(research_id=pk)
            note_formset = NoteFormset(queryset=research_notes)
            note_formset.extra = number_of_fields - len(research_notes)
        else:
            form = ModelForm()
            note_formset = NoteFormset(queryset=Note.objects.none())

    context.update(csrf(request))
    context['form'] = form
    context['note_formset'] = note_formset

    return render_to_response("research/form.html", context, context_instance=RequestContext(request))


@login_required
def details(request, pk):
    return get_details(request, model, model_form, pk, context, "common/details.html")

@login_required
def delete(request, pk):
    return get_delete(request, model, pk, "/research/")