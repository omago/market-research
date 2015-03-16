# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'NoteType'
        db.create_table('note_type', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal(u'note_type', ['NoteType'])


    def backwards(self, orm):
        # Deleting model 'NoteType'
        db.delete_table('note_type')


    models = {
        u'note_type.notetype': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'NoteType', 'db_table': "'note_type'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['note_type']