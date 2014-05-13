#-*- coding: utf-8 -*-
from django.conf.urls import *
from django.views.generic import TemplateView

urlpatterns = patterns('contato.views',
    url(r'^contato$', 'contato', name='contato'),
    
    url(r'^contato-resposta.html', TemplateView.as_view(template_name='contato/contato-resposta.html'), name='contato-resposta'),
)

