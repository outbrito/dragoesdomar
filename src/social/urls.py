# -*- coding: utf-8 -*-
from django.conf.urls import url, patterns

urlpatterns = patterns('social.views',
    url(r'^social/(?P<_type>(facebook|twitter|instagram))/$', 'social', name="social"),    
)