# -*- coding: UTF-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.core.urlresolvers import reverse
from django.contrib.contenttypes.generic import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


RAMOS = (
    ('lob', 'Lobinho'),
    ('esc', 'Escoteiro'),
    ('lob', 'Sênior'),
    ('lob', 'Pioneiro'),
)

# class BlogPost(models.Model):
#     class Meta:
#         verbose_name = u"Post de Blog"
#         verbose_name_plural = u"Posts de Blog"
#         ordering = ("-publicacao",)
#         
#     publicacao = models.DateTimeField(u"Data de Publicação", auto_now_add=True, editable=False)
#     ultima_modificacao = models.DateTimeField(u"Ultima Modificação", auto_now_add=True, auto_now=True, editable=False)
#     usuario = models.ForeignKey(User)
#     
#     titulo = models.CharField(u"Título do Post", help_text="Titulo do Post", max_length=100)
#     texto = models.TextField(u"Texto do Post", help_text="Texto do Post")
 

class Secao(models.Model):
    class Meta:
        verbose_name = u"Seção"
        verbose_name_plural = u"Seções"
        ordering = ("order",)
        
    order = models.PositiveSmallIntegerField("Ordem", help_text="Ordenação no Menu")
    ativa = models.BooleanField("Ativa?", default=True)
    slug = models.SlugField(u"URL da Seção")
    
    ramo = models.CharField(u"Ramo", help_text=u"Ramo da Seção (por faixa etária)", max_length=3, choices=RAMOS)
    nome = models.CharField(u"Nome", help_text=u"Nome da Seção", max_length=50)
    descricao = models.TextField(u"Descrição/Historia", help_text=u"Descrição e história da seção")
    imagem = models.ImageField(u"Imagem", help_text=u"Imagem ou logotipo da seção", blank=True, null=True, upload_to="secoes/imagens")
    
    def get_absolute_url(self):
        return reverse('secao', kwargs={'slug': self.slug})
    
    def __unicode__(self):
        return self.nome
    

class ArquivoSecao(models.Model):
    class Meta:
        verbose_name = u"Arquivo da Seção"
        verbose_name_plural = u"Arquivos da Seção"
        ordering = ("-publicacao",)
    
    publicacao = models.DateTimeField(u"Data de Publicação", auto_now_add=True, editable=False)
    secao = models.ForeignKey(Secao, related_name="arquivos")
    arquivo = models.FileField(u"Arquivo", help_text="Adicione um arquivo para disponibilizar no site...", upload_to="secoes/fotos")


class FotoSecao(models.Model):
    class Meta:
        verbose_name = u"Foto da Seção"
        verbose_name_plural = u"Fotos da Seção"
        ordering = ("-publicacao",)
        
    publicacao = models.DateTimeField(u"Data de Publicação", auto_now_add=True, editable=False)
    secao = models.ForeignKey(Secao, related_name="fotos")
    foto = models.ImageField(u"Foto", help_text="Adicione uma imagem p/ exibir na galeria...", upload_to="secoes/fotos")
    


class Patrulha(models.Model):
    class Meta:
        verbose_name = u"Patrulha/Equipe"
        verbose_name_plural = u"Patrulhas/Equipes"
        ordering = ("nome",)
        
    secao = models.ForeignKey(Secao, related_name="patrulhas")
    ativa = models.BooleanField("Ativa?", default=True)
    slug = models.SlugField(u"URL da Patrulha")
    
    nome = models.CharField(u"Nome", help_text=u"Nome da Patrulha", max_length=50)
    descricao = models.TextField(u"Descrição/Historia", help_text=u"Descrição e história da patrulha")
    imagem = models.ImageField(u"Imagem", help_text=u"Imagem ou logotipo da patrulha", blank=True, null=True, upload_to="secoes/patrulhas/imagens")    
    
    def get_absolute_url(self):
        return reverse('patrulha', kwargs={'slug_secao': self.secao.slug, 'slug': self.slug})
    
    def __unicode__(self):
        return self.nome
    
    def _actions(self):
        acoes = u"<a style=\"padding-left: 7px;\" href=\"%s\"><img src=\"%sadmin/img/admin/icon_changelink.gif\" />%s</a>" % (self.pk, settings.STATIC_URL, u"Editar")
        acoes += u"<a style=\"padding-left: 7px;\" href=\"%s\"><img src=\"%sadmin/img/admin/selector-addall.gif\" />%s</a>" % (self.get_absolute_url(), settings.STATIC_URL, u"Ver no site")
        acoes += u"<a style=\"padding-left: 7px;\" href=\"javascript://\" onClick=\"(function($) { $('input:checkbox[name=_selected_action]').attr('checked', ''); $('input:checkbox[name=_selected_action][value=%s]').attr('checked', 'checked'); $('select[name=action]').attr('value', 'delete_selected'); $('#changelist-form').submit(); })(jQuery);\" ><img src=\"%sadmin/img/admin/icon_deletelink.gif\" />%s</a>" % (self.pk, settings.STATIC_URL, u"Remover")
        return acoes
    _actions.allow_tags = True
    _actions.short_description = u"Ações"
    
    
class ArquivoPatrulha(models.Model):
    class Meta:
        verbose_name = u"Arquivo da Patrulha"
        verbose_name_plural = u"Arquivos da Patrulha"
        ordering = ("-publicacao",)
        
    publicacao = models.DateTimeField(u"Data de Publicação", auto_now_add=True, editable=False)
    secao = models.ForeignKey(Patrulha, related_name="arquivos")
    arquivo = models.FileField(u"Arquivo", help_text="Adicione um arquivo para disponibilizar no site...", upload_to="secoes/patrulha/arquivos")


class FotoPatrulha(models.Model):
    class Meta:
        verbose_name = u"Foto da Seção"
        verbose_name_plural = u"Fotos da Seção"
        ordering = ("-publicacao",)
        
    publicacao = models.DateTimeField(u"Data de Publicação", auto_now_add=True, editable=False)
    secao = models.ForeignKey(Patrulha, related_name="fotos")
    foto = models.ImageField(u"Foto", help_text="Adicione uma imagem p/ exibir na galeria...", upload_to="secoes/patrulha/fotos")