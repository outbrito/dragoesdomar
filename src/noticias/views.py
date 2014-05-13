# -*- coding:utf-8 -*-
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.http import Http404
from datetime import datetime
from django.core.paginator import Paginator, EmptyPage

from noticias.models import Artigo



def noticias(request, template_name="noticias/noticias.html"):
    articles_list = Artigo.objects.publisheds()
    destaques = Artigo.objects.publisheds(destaque=True)

    if request.GET.get('tag'):
        articles_list = articles_list.filter(tags__icontains=request.GET.get('tag'))

    paginator = Paginator(articles_list, 10)
    try: page = int(request.GET.get('page', 1))
    except: page = 1
    
    try: artigos = paginator.page(page)
    except EmptyPage: raise Http404

    return render_to_response(template_name, {
        'destaques': destaques,
        'artigos': artigos,
    },context_instance=RequestContext(request))


def noticia(request, slug, template_name="noticias/noticia.html"):
    artigo = get_object_or_404(Artigo, slug=slug, is_published=True, data__lte=datetime.now())

    return render_to_response(template_name, {
        'artigo': artigo,
    }, context_instance=RequestContext(request))