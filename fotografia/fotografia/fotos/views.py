from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import View, ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from fotos.models import *


def principal(request):
    return render_to_response('index.html',context_instance=RequestContext(request))

def galeria(request):
    return render_to_response('base.html',context_instance=RequestContext(request))

def album(request,titulo):
    albumes=FotosHugo.objects.filter(galerias=titulo[:5])
    fotografias=[]
    galeria=""
    for identificador in albumes:
        if FotosAdjuntas.objects.filter(relacion=identificador.id):
            fotografias.append(FotosAdjuntas.objects.filter(relacion=identificador.id)[0])
            galeria=identificador.get_galerias_display().lower()
    paginator= Paginator(albumes,3)
    pagina=request.GET.get("page")
    try:
        listaAlbumes = paginator.page(pagina)
    except PageNotAnInteger:
        #si no es un entero la pagina
        listaAlbumes=paginator.page(1)
    except EmptyPage:
        #si esta vacia la pagina
        listaAlbumes=paginator.page(paginator.num_pages)
    
    return render_to_response("galeria.html",{"albumes":listaAlbumes,"fotografias":fotografias,"galeria":galeria},context_instance=RequestContext(request))

def listaFotos(request,album,titulo):
    albumes=FotosHugo.objects.filter(urlTitulo=album)
    fotografias=FotosAdjuntas.objects.filter(relacion=albumes[0].id)
    paginator= Paginator(fotografias,1)
    pagina=request.GET.get("page")
    try:
        listaFotos = paginator.page(pagina)
    except PageNotAnInteger:
        #si no es un entero la pagina
        listaFotos=paginator.page(1)
    except EmptyPage:
        #si esta vacia la pagina
        listaFotos=paginator.page(paginator.num_pages)
    
    return render_to_response('fotografias.html',{"fotografias":listaFotos},context_instance=RequestContext(request))

