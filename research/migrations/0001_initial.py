# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Research'
        db.create_table('research', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['project.Project'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal(u'research', ['Research'])


    def backwards(self, orm):
        # Deleting model 'Research'
        db.delete_table('research')


    models = {
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

    complete_apps = ['research']