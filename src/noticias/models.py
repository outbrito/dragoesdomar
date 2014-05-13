# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings
from datetime import datetime
from django.db.models import signals
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from tagging_autocomplete_tagit.models import TagAutocompleteTagItField



class ArtigoManager(models.Manager):
    def publisheds(self, **kwargs):
        return self.filter(is_published=True, data__lte=datetime.now(), **kwargs).order_by('-data')
    
class Artigo(models.Model):

    class Meta:
        ordering = ('-data', )
        verbose_name = u"Artigo"
        verbose_name_plural = u"Artigos"

    titulo = models.CharField(u"Título", max_length=160, help_text=u"Informe um título para o artigo.")
    imagem = models.ImageField(u"Imagem", max_length=255, upload_to="artigos", blank=True, null=True, help_text=u"Selecione uma imagem para o artigo.")
    slug = models.SlugField(u"Slug", max_length=255, blank=True, unique=True)
    conteudo = models.TextField(u"Conteúdo", help_text=u"Escreva o conteúdo do artigo.")
    tags = TagAutocompleteTagItField(u'Tags')
    autor = models.ForeignKey(User, verbose_name=u"Usuário", blank=True)
    is_published = models.BooleanField(u"Publicado?", choices=((True,"Publicado"), (False, "Rascunho")), default=True, help_text=u"Marque \"Publicado\" para exibir o artigo no site.")
    destaque = models.BooleanField(u"Destaque?", choices=((True,"Destaque"), (False, "Noticia normal")), default=True, help_text=u"Marque \"Destaque\" para exibir o artigo nos destaques do site.")
    data = models.DateTimeField(u"Data de publicação", default=datetime.now)
    comentarios = models.BooleanField(u"Habilitar comentários?", default=True, help_text=u"Marque para permitir os comentários no artigo.")
    fonte = models.CharField(u"Fonte", max_length=160, blank=True, null=True, help_text=u"Informe um fonte para o artigo.")
    
    objects = ArtigoManager()

    def _actions(self):
        acoes = u"<div style=\"width: 300px\">"
        acoes += u"<a style=\"padding-left: 7px;\" href=\"%s\"><img src=\"%sadmin/img/admin/icon_changelink.gif\" />%s</a>" % (self.pk, settings.STATIC_URL, u"Editar")
        acoes += u"<a style=\"padding-left: 7px;\" href=\"javascript://\" onClick=\"(function($) { $('input:checkbox[name=_selected_action]').attr('checked', ''); $('input:checkbox[name=_selected_action][value=%s]').attr('checked', 'checked'); $('select[name=action]').attr('value', 'delete_selected'); $('#changelist-form').submit(); })(jQuery);\" ><img src=\"%sadmin/img/admin/icon_deletelink.gif\" />%s</a>" % (self.pk, settings.STATIC_URL, u"Remover")
        if self.is_published:
            acoes += u"<a style=\"padding-left: 7px;\" href=\"javascript://\" onClick=\"(function($) { $('input:checkbox[name=_selected_action]').attr('checked', ''); $('input:checkbox[name=_selected_action][value=%s]').attr('checked', 'checked'); $('select[name=action]').attr('value', 'make_unpublished'); $('#changelist-form').submit(); })(jQuery);\" ><img src=\"%sadmin/img/admin/icon_error.gif\" />%s</a>" % (self.pk, settings.STATIC_URL, u"Despublicar")
            acoes += u"<a style=\"padding-left: 7px;\" href=\"%s\"><img src=\"%sadmin/img/admin/selector-addall.gif\" />%s</a>" % (self.get_absolute_url(), settings.STATIC_URL, u"Ver no site")
        else:
            acoes += u"<a style=\"padding-left: 7px;\" href=\"javascript://\" onClick=\"(function($) { $('input:checkbox[name=_selected_action]').attr('checked', ''); $('input:checkbox[name=_selected_action][value=%s]').attr('checked', 'checked'); $('select[name=action]').attr('value', 'make_published'); $('#changelist-form').submit(); })(jQuery);\" ><img src=\"%sadmin/img/admin/icon_success.gif\" />%s</a>" % (self.pk, settings.STATIC_URL, u"Publicar")
            acoes += u"<a style=\"padding-left: 7px;\" class=\"lightbox\" href=\"%s?lightbox[width]=800&lightbox[height]=600&lightbox[iframe]=true\"><img src=\"%sadmin/img/admin/selector-addall.gif\" />%s</a>" % (self.get_preview_url(), settings.STATIC_URL, u"Preview")
        acoes += u"</div>"
        return acoes
    _actions.allow_tags = True
    _actions.short_description = u"Ações"

    def __unicode__(self):
        return self.titulo
    
    def get_absolute_url(self):
        return reverse('noticia', kwargs={'slug': self.slug, })
    
    def get_full_url(self):
        return "%s%s" % (settings.HOST, self.get_absolute_url(), )
    
    def fb_comments(self):
        return u'<fb:comments-count href="%s%s"></fb:comments-count>' % (settings.HOST, self.get_absolute_url(), )
    fb_comments.short_description = u'Comentários'
    fb_comments.allow_tags = True
        

def article_slug_pre_save(signal, instance, sender, **kwargs):
    if not instance.slug:
        slug = slugify(instance.titulo)
        new_slug = slug
        counter = 0
        while Artigo.objects.filter(slug=new_slug).exclude(id=instance.id).count() > 0:
            counter += 1
            new_slug = '%s-%d'%(slug, counter)
        instance.slug = new_slug
signals.pre_save.connect(article_slug_pre_save, sender=Artigo)