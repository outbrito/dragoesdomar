# -*- coding: utf-8 -*-
from django.contrib import admin
from suit.admin import SortableModelAdmin
from models import Secao, Patrulha


class PatrulhaAdminInline(admin.TabularInline):
    prepopulated_fields = {"slug": ("nome",)}
    fields = ['ativa', 'nome', 'slug',]
    extra = 1
    max_num = 4
    model = Patrulha
        

class SecaoAdmin(SortableModelAdmin):
    sortable = 'order'
    prepopulated_fields = {"slug": ("nome",)}
    
    inlines = (PatrulhaAdminInline,)
    
    class Media:
        js = (
            'tinymce/tinymce.min.js',
            'tinymce/tinymce_init.js',
        )
        

class PatrulhaAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("nome",)}
    list_display = ("nome", "_actions",)
    readonly_fields = ["_actions"]
    
    class Media:
        js = (
            'tinymce/tinymce.min.js',
            'tinymce/tinymce_init.js',
        )


admin.site.register(Secao, SecaoAdmin)
admin.site.register(Patrulha, PatrulhaAdmin)