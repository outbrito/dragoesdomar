'''
Created on 12/02/2014

@author: Thiago
'''
from django.contrib import admin
from models import Evento

class EventoAdmin(admin.ModelAdmin):
    fields = ('tipo', 'title', 'start', 'end', )
    list_display = ('pk', 'tipo', 'title', 'start', 'end', )
    list_editable = ('tipo', 'title', 'start', 'end', )
        
admin.site.register(Evento, EventoAdmin)
