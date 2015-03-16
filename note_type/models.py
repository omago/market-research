#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models


class NoteType(models.Model):
    name = models.CharField(max_length=128, verbose_name="Naziv")

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['-pk']
        db_table = "note_type"