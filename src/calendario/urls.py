#-*- coding: utf-8 -*-
from django.conf.urls import *

urlpatterns = patterns('calendario.views',
    url(r'^calendario', 'calendario', name='calendario'),
    
)

