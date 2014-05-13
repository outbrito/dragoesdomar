# -*- coding: utf-8 -*-
from django import forms
from django.template import RequestContext, loader
from django.conf import settings

from send_email.functions import send_template_mail


class ContatoForm(forms.Form):

    nome = forms.CharField()
    email = forms.EmailField()
    assunto = forms.CharField()
    mensagem = forms.CharField(widget=forms.Textarea)

    def send_email(self, request):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']
        
        #Email para os contatos
        t = loader.get_template('contato/email.html')
        html_content = t.render(RequestContext(request, {
            'titulo': u"Formulário de contato",
            'nome': nome,
            'email': email,
            'assunto': assunto,
            'mensagem': mensagem,
        }))
        send_template_mail(
            subject=u"Formulário de contato",
            html_content=html_content,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=settings.CONTACTS
        )

        #Email para quem enviou
        send_template_mail(
            subject=u"Recebemos o seu contato",
            html_content=u"<h1>Recebemos o seu contato, assim que possível entraremos em contato.</h1>",
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[email, ]
        )