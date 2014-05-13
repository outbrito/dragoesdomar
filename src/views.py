# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from noticias.models import Artigo


def home(request, template='index.html'):
    destaques = Artigo.objects.publisheds(destaque=True)[:4]
    noticias = Artigo.objects.publisheds()[:5]

    return render_to_response(template,
                               {
                                'destaques': destaques,
                                'noticias': noticias
                                },
                               context_instance=RequestContext(request)
                               )
