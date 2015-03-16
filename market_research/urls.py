#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the next line to enable the admin:
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'core/static/'}),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^/*', include("note.urls")),
    url(r'^/*', include("note_type.urls")),
    url(r'^/*', include("research.urls")),
    url(r'^/*', include("project.urls")),
    url(r'^/*', include("core.urls")),
)