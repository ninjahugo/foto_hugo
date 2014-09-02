from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('fotos.views',
     url(r'^index/$', 'principal'),
     url(r'^index/galerias/$', 'galeria'),
     url(r'^index/galerias/(?P<titulo>\w+)$', 'album'),
     url(r'^index/galerias/(?P<titulo>\w+)/(?P<album>\w+)/$', 'listaFotos'),
     url(r'^index/galerias/(?P<titulo>\w+)/(?P<album>[\w-]+)/$', 'listaFotos'),
)
