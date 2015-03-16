# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Note'
        db.create_table('note', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('research', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['research.Research'])),
            ('note_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['note_type.NoteType'])),
            ('note', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'note', ['Note'])


    def backwards(self, orm):
        # Deleting model 'Note'
        db.delete_table('note')


    models = {
        u'note.note': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'Note', 'db_table': "'note'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'note': ('django.db.models.fields.TextField', [], {}),
            'note_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['note_type.NoteType']"}),
            'research': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['research.Research']"})
        },
        u'note_type.notetype': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'NoteType', 'db_table': "'note_type'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'project.project': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'Project', 'db_table': "'project'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'research.research': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'Research', 'db_table': "'research'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['project.Project']"}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['note']