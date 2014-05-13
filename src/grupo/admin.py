'''
Created on 02/02/2014

@author: Thiago
'''
from django.contrib import admin
from models import CategoriaArquivo, Arquivo


class ArquivoAdminInline(admin.TabularInline):
    model = Arquivo

class CategoriaArquivoAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("nome",)}
    model = CategoriaArquivo
    
    inlines = (ArquivoAdminInline,)
    
    
admin.site.register(CategoriaArquivo, CategoriaArquivoAdmin)


#Workaround below
from chunks.admin import ChunkAdmin
from chunks.models import Chunk 

class BetterChunkAdmin(ChunkAdmin):
    class Media:
        js = (
            'tinymce/tinymce.min.js',
            'tinymce/tinymce_init.js',
        )
        
admin.site.unregister(Chunk)
admin.site.register(Chunk, BetterChunkAdmin)
