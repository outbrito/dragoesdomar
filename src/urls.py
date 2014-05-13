from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^tagging_autocomplete_tagit/', include('tagging_autocomplete_tagit.urls')),
    url(r'^calendar/', include('django_bootstrap_calendar.urls')),
)

urlpatterns += patterns('',
    url(r'^$', 'views.home', name='home'),
    
    url(r'^', include('grupo.urls')),
    url(r'^', include('noticias.urls')),
    url(r'^', include('social.urls')),
    url(r'^', include('contato.urls')),
    url(r'^', include('calendario.urls')),
    url(r'^', include('secoes.urls')),
)

urlpatterns += patterns('django.contrib.flatpages.views',
    (r'^(?P<url>.*/)$', 'flatpage'),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
