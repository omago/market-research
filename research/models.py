#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models

from project.models import Project


class Research(models.Model):
    project = models.ForeignKey(Project, verbose_name="Projekt")
    name = models.CharField(max_length=128, verbose_name="Naziv")
    url = models.CharField(max_length=128, verbose_name="Url")

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['-pk']
        db_table = "research"