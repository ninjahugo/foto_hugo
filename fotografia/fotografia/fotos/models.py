# -*- coding: cp1252 -*-
from django.db import models
from django.template.defaultfilters import slugify
from django.core.files.storage import FileSystemStorage
import os

FOTOS_CHOICES=(
    ("paisa","Paisajes"),
    ("depor","Deportes"),
    ("retra","Retratos"),
    ("comid","Comidas"),
    ("music","Musica"),

    )
class FotosHugo(models.Model):
    urlTitulo=models.SlugField(db_index=True)
    album=models.CharField(max_length=100,unique=True)
    galerias= models.CharField(max_length=5, choices=FOTOS_CHOICES)
    class Meta:
        verbose_name_plural = u"Fotografías"
        
    def __unicode__(self):
        return "%s" % self.album

    def get_absolute_url(self):
        return "http://127.0.0.1:8000/index/galerias/%s/%s/" % (self.get_galerias_display().lower(),self.urlTitulo)

    def save(self):
        self.urlTitulo = slugify(self.album)
        super(FotosHugo, self).save()

class FotosAdjuntas(models.Model):
#always in python add 'u' before of save
    path='C:/Users/7/Desktop/fotografia/fotografia/fotografia/media/archivos/fotos/'
    fotos=models.ImageField(upload_to='archivos/fotos')
    relacion=models.ForeignKey(FotosHugo)
    class Meta:
        verbose_name_plural = "Fotos"
   
    def __unicode__(self):
        return u"%s" % (self.fotos)    

#    def save(self):
#        archivo=FileSystemStorage(self.path+str(self.fotos))
#        if archivo.exists(self.fotos):
#            print "existe"
#        pass
