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

HOST = 'http://novocasatudo.sodateste.com.br'

JS_DIR = STATIC_URL + 'site/js/'

CONTACTS = ()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'soda_novocasatudo',
        'USER': 'soda_novocasatud',
        'PASSWORD': 's0d4!SODA@',
        'HOST': '',
        'PORT': '',
    }
}

ECOMMERCE_ADMINS = ('thiago.paiva@sodavirtual.com.br', 'casatudo@casatudo.com.br',)
ECOMMERCE_CORREIOS_CEP_ORIGEM = '58028050'