from django.db import models

# Create your models here.

class CategoriaArquivo(models.Model):
    class Meta:
        verbose_name = "Categoria de Arquivo"
        verbose_name_plural = "Arquivos p/ Categoria"
        
    nome = models.CharField(u'Nome da Categoria', max_length=50)
    order = models.PositiveSmallIntegerField(u"Ordem")
    ativo = models.BooleanField(u"Ativo?", default=False)
    
    slug = models.SlugField(u"Slug")
    
    def __unicode__(self):
        return self.nome


class Arquivo(models.Model):
    categoria = models.ForeignKey(CategoriaArquivo, related_name="arquivos")
    nome = models.CharField(u"Nome do arquivo", max_length=50)
    arquivo = models.FileField(u"Arquivo", upload_to="grupo/arquivos")
    
    def __unicode__(self):
        return self.nome
        
    