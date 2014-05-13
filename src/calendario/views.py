# -*- coding: utf-8 -*-
# Python Imports
# Django Imports
from django.shortcuts import render_to_response
from django.template import RequestContext
# Project Imports

    
def calendario(request, template='calendario/calendario.html'):
    return render_to_response(template,
                               {                                
                                }, 
                               context_instance=RequestContext(request)
                               )