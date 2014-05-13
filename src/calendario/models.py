# -*- coding: utf-8 -*-

from django.db import models
from django_bootstrap_calendar.models import CalendarEvent

# Create your models here.


class Evento(CalendarEvent):
    class Meta:
        verbose_name = u'Evento'
        verbose_name_plural = u'Eventos'
        ordering = ('start',)
    
    TIPO_EVENTO = [
        ('evento-mundial', u'Mundial'),
        ('evento-nacional', u'Nacional'),
        ('evento-regional', u'Regional'),
        ('evento-grupo', u'Grupo'),
        ('evento-tropa', u'Tropa'),
        ('evento-patrulha', u'Patrulha'),
    ]
    
    tipo = models.CharField(max_length=20, verbose_name=u'Tipo de Evento', choices=TIPO_EVENTO)
    
    def save(self):
        self.css_class = self.tipo
        super(Evento, self).save()