# -*- coding: utf-8 -*-
# Python Imports
# Django Imports
from django.shortcuts import render_to_response
from django.template import RequestContext
# Project Imports
from models import CategoriaArquivo

    
def grupo(request, template='grupo/grupo.html'):
    return render_to_response(template,
                               {
                                "categorias": CategoriaArquivo.objects.all()
                                }, 
                               context_instance=RequestContext(request)
                               )