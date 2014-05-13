# -*- coding: utf-8 -*-
from django.conf.urls import *

urlpatterns = patterns('noticias.views',
    url(r'^noticias/$', 'noticias', name="noticias"),
    url(r'^noticias/(?P<slug>[\w_-]+)/$', 'noticia', name="noticia"),
)