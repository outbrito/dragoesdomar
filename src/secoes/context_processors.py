# -*- coding: UTF-8 -*-

'''
Created on 18/02/2014

@author: Thiago
'''
from models import Secao

def main(request):
    secoes = Secao.objects.all()
    return {'secoes': secoes}