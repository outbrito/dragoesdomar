# -*- coding: UTF-8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns('secoes.views',
    url(r'^(?P<slug>[\w_-]+)/$', 'secao', name="secao"),
    url(r'^(?P<slug_secao>[\w_-]+)/(?P<slug>[\w_-]+)/$', 'patrulha', name="patrulha"),
)
