# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CategoriaArquivo'
        db.create_table(u'grupo_categoriaarquivo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('order', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('ativo', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
        ))
        db.send_create_signal(u'grupo', ['CategoriaArquivo'])

        # Adding model 'Arquivo'
        db.create_table(u'grupo_arquivo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('categoria', self.gf('django.db.models.fields.related.ForeignKey')(related_name='arquivos', to=orm['grupo.CategoriaArquivo'])),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('arquivo', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal(u'grupo', ['Arquivo'])


    def backwards(self, orm):
        # Deleting model 'CategoriaArquivo'
        db.delete_table(u'grupo_categoriaarquivo')

        # Deleting model 'Arquivo'
        db.delete_table(u'grupo_arquivo')


    models = {
        u'grupo.arquivo': {
            'Meta': {'object_name': 'Arquivo'},
            'arquivo': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'categoria': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'arquivos'", 'to': u"orm['grupo.CategoriaArquivo']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'grupo.categoriaarquivo': {
            'Meta': {'object_name': 'CategoriaArquivo'},
            'ativo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'order': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['grupo']