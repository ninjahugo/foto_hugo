# -*- coding: cp1252 -*-
from django.contrib import admin
from fotos.models import *
from django.core.exceptions import ValidationError


#otra forma de registrar es @admin.register(nombreDelModelo)

class FotosAdjuntasInline(admin.StackedInline):
    model = FotosAdjuntas
    extra = 1

class AlbumAdmin(admin.ModelAdmin):
    model = FotosHugo
    inlines = [FotosAdjuntasInline]
    list_display = ('album',)
    exclude=('urlTitulo',)




admin.site.register(FotosHugo,AlbumAdmin)

