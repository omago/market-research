#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models

from research.models import Research
from note_type.models import NoteType


class Note(models.Model):
    research = models.ForeignKey(Research, verbose_name="Projekt")
    note_type = models.ForeignKey(NoteType, verbose_name="Tip bilješke")
    note = models.TextField(verbose_name="Bilješka")


    def __unicode__(self):
        return self.note

    class Meta:
        ordering = ['-pk']
        db_table = "note"