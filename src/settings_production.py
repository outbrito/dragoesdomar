# -*- coding: utf-8 -*-
# Load settings first
try:
    from settings import *
except ImportError:
    pass

# Now override any of them
LOCAL = False
DEBUG = False
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dragoesdomar',
        'USER': 'root',
        'PASSWORD': 'dragoes@DR@G035!',
        'HOST': '',
        'PORT': '',
    }
}

ALLOWED_HOSTS = ['127.0.0.1', '10.1.0.23']
