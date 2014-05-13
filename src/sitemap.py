# -*- encoding: utf-8 -*-
from django.contrib.sitemaps import Sitemap
from ecommerce.models import Produto
from src.site.models import Receita

from django.core.urlresolvers import reverse

class StaticSitemap(Sitemap):
    priority = 0.5
    lastmod = None
 
    def items(self):
        return [
            (reverse('index'), "daily"),
            (reverse('receitas'), "daily"),
            (reverse('produtos'), "daily"),
            reverse('contato'),
            reverse('sobre'),
            reverse('busca'),
        ]
 
    def location(self, obj):
        return obj[0] if isinstance(obj, tuple) else obj
 
    def changefreq(self, obj):
        return obj[1] if isinstance(obj, tuple) else "monthly"


class ReceitasSitemap(Sitemap):
    priority = 0.5
    changefreq = "daily"
 
    def location(self, obj):
        return obj.get_absolute_url()
 
    def items(self):
        return Receita.objects.all()


class ProdutosSitemap(Sitemap):
    priority = 0.5
    changefreq = "daily"
 
    def location(self, obj):
        return obj.get_absolute_url()

    def lastmod(self, obj):
        return obj.data_modificacao
 
    def items(self):
        return Produto.objects.ativos()


sitemaps = dict(
    static = StaticSitemap,
    receitas = ReceitasSitemap,
    produtos = ProdutosSitemap,
)