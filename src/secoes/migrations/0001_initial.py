# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Secao'
        db.create_table(u'secoes_secao', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('order', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('ativa', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('ramo', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('descricao', self.gf('django.db.models.fields.TextField')()),
            ('imagem', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'secoes', ['Secao'])

        # Adding model 'ArquivoSecao'
        db.create_table(u'secoes_arquivosecao', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('publicacao', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('secao', self.gf('django.db.models.fields.related.ForeignKey')(related_name='arquivos', to=orm['secoes.Secao'])),
            ('arquivo', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal(u'secoes', ['ArquivoSecao'])

        # Adding model 'FotoSecao'
        db.create_table(u'secoes_fotosecao', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('publicacao', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('secao', self.gf('django.db.models.fields.related.ForeignKey')(related_name='fotos', to=orm['secoes.Secao'])),
            ('foto', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'secoes', ['FotoSecao'])

        # Adding model 'Patrulha'
        db.create_table(u'secoes_patrulha', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('secao', self.gf('django.db.models.fields.related.ForeignKey')(related_name='patrulhas', to=orm['secoes.Secao'])),
            ('ativa', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('descricao', self.gf('django.db.models.fields.TextField')()),
            ('imagem', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'secoes', ['Patrulha'])

        # Adding model 'ArquivoPatrulha'
        db.create_table(u'secoes_arquivopatrulha', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('publicacao', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('secao', self.gf('django.db.models.fields.related.ForeignKey')(related_name='arquivos', to=orm['secoes.Patrulha'])),
            ('arquivo', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal(u'secoes', ['ArquivoPatrulha'])

        # Adding model 'FotoPatrulha'
        db.create_table(u'secoes_fotopatrulha', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('publicacao', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('secao', self.gf('django.db.models.fields.related.ForeignKey')(related_name='fotos', to=orm['secoes.Patrulha'])),
            ('foto', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'secoes', ['FotoPatrulha'])


    def backwards(self, orm):
        # Deleting model 'Secao'
        db.delete_table(u'secoes_secao')

        # Deleting model 'ArquivoSecao'
        db.delete_table(u'secoes_arquivosecao')

        # Deleting model 'FotoSecao'
        db.delete_table(u'secoes_fotosecao')

        # Deleting model 'Patrulha'
        db.delete_table(u'secoes_patrulha')

        # Deleting model 'ArquivoPatrulha'
        db.delete_table(u'secoes_arquivopatrulha')

        # Deleting model 'FotoPatrulha'
        db.delete_table(u'secoes_fotopatrulha')


    models = {
        u'secoes.arquivopatrulha': {
            'Meta': {'ordering': "('-publicacao',)", 'object_name': 'ArquivoPatrulha'},
            'arquivo': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'publicacao': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'secao': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'arquivos'", 'to': u"orm['secoes.Patrulha']"})
        },
        u'secoes.arquivosecao': {
            'Meta': {'ordering': "('-publicacao',)", 'object_name': 'ArquivoSecao'},
            'arquivo': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'publicacao': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'secao': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'arquivos'", 'to': u"orm['secoes.Secao']"})
        },
        u'secoes.fotopatrulha': {
            'Meta': {'ordering': "('-publicacao',)", 'object_name': 'FotoPatrulha'},
            'foto': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'publicacao': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'secao': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'fotos'", 'to': u"orm['secoes.Patrulha']"})
        },
        u'secoes.fotosecao': {
            'Meta': {'ordering': "('-publicacao',)", 'object_name': 'FotoSecao'},
            'foto': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'publicacao': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'secao': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'fotos'", 'to': u"orm['secoes.Secao']"})
        },
        u'secoes.patrulha': {
            'Meta': {'ordering': "('nome',)", 'object_name': 'Patrulha'},
            'ativa': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'descricao': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagem': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'secao': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'patrulhas'", 'to': u"orm['secoes.Secao']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        },
        u'secoes.secao': {
            'Meta': {'ordering': "('order',)", 'object_name': 'Secao'},
            'ativa': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'descricao': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagem': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'order': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'ramo': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['secoes']