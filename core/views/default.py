#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import date

from django.utils import timezone
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.contrib.auth.models import User

@login_required
def index(request):
    context = {'page_title': "Početna"}

    return render_to_response('default/index.html', context, context_instance=RequestContext(request))


@login_required
def access_denied(request):
    context = {'page_title': "ACCESS DENIED"}
    return render_to_response('default/access_denied.html', context, context_instance=RequestContext(request))
