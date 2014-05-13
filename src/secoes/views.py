# -*- coding: UTF-8 -*-
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from models import Secao, Patrulha

def secao(request, slug, template_name="secoes/secao.html"):
    secao = get_object_or_404(Secao, slug=slug)

    return render_to_response(template_name, {
        'secao': secao,
    }, context_instance=RequestContext(request))

    
def patrulha(request, slug_secao, slug, template_name="secoes/patrulha.html"):
    patrulha = get_object_or_404(Patrulha, slug=slug, secao__slug=slug_secao)

    return render_to_response(template_name, {
        'patrulha': patrulha,
    }, context_instance=RequestContext(request))