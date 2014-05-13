# -*- coding: utf-8 -*-
from django.contrib import admin
from django.conf import settings
from models import Artigo


def make_published(modeladmin, request, queryset):
    queryset.updata(is_published=True)
    
def make_unpublished(modeladmin, request, queryset):
    queryset.updata(is_published=False)
    
class ArtigoAdmin(admin.ModelAdmin):

    list_display = ("titulo", "is_published", "data", "fb_comments", "_actions",)
    search_fields = ("titulo", )
    list_filter = ("autor", "is_published",  "data", )
    save_on_top = True
    
    actions = (make_published, make_unpublished)

    class Media:
        js = (
            'tinymce/tinymce.min.js',
            'tinymce/tinymce_init.js',
        )
        
    fieldsets = [
        (u'Artigo',                   {'fields' : ("titulo", "imagem", ), }, ),
        (u'Conteúdo',                 {'fields' : ("conteudo", "tags" ), }, ),
        (u'Opções',                   {'fields' : ("data", "is_published", "destaque", "comentarios", "fonte", ), }, ),
    ]

    def save_model(self, request, obj, form, change):
        if not change:
            obj.autor = request.user
        super(ArtigoAdmin, self).save_model(request, obj, form, change)

admin.site.register(Artigo, ArtigoAdmin)