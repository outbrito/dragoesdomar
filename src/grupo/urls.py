#-*- coding: utf-8 -*-
from django.conf.urls import *

urlpatterns = patterns('grupo.views',
    url(r'^grupo', 'grupo', name='grupo'),
    
)

