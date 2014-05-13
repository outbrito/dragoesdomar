#-*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.http import HttpResponse
from django.utils import simplejson

from forms import ContatoForm


def contato(request, form_class=ContatoForm, msg='', template_name="contato/contato.html"):
    if request.method == 'GET':
        form = form_class()
        
        ret = render_to_response(template_name, 
                                 {
                                  'form':form,
                                  'msg': msg,
                                  },
                                 context_instance=RequestContext(request)
                                 )
        
    elif request.method == 'POST':
        response = {
            'status' : 'error',
        }
        form = form_class(request.POST)

        #valida o formulario
        if form.is_valid():
            #envia o email
            form.send_email(request)
            response['status'] = 'success'

        ret = render_to_response(
                                 template_name, 
                                 {
                                  'form':form,
                                  'msg': msg,
                                  },
                                 context_instance=RequestContext(request))

    return ret