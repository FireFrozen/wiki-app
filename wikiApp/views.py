from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import HttpRequest
from .models import temaWiki,articuloWiki

# Create your views here.

# listaTemas = [{'nombreTema':'Tema 1', 'descripcionTema': 'Descripcion1'},
#             {'nombreTema':'Tema 2', 'descripcionTema': 'Descripcion2'}]

def index(request):
    return render(request, 'homepage.html')

def crearNuevoTema(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')

        temaWiki.objects.create(
            nombre = nombre,
            descripcion = descripcion,
        )
        return HttpResponseRedirect(reverse('wikiApp:homepage'))
    return render(request, 'crearNuevoTema.html')


def crearNuevoArticulo(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        tema_id = request.POST['temaRelacionado']
        temaRelacionado = temaWiki.objects.get(id=tema_id)
        contenido = request.POST.get('contenido')

        articuloWiki.objects.create(
            titulo = titulo,
            temaRelacionado = temaRelacionado,
            contenido = contenido,
        )

    listaTemas = temaWiki.objects.all()
    # listaArticulos= articuloWiki.objects.all()
    # print(listaTemas[0].nombre)
    # print(listaArticulos[0].titulo)

    return render(request, 'crearNuevoArticulo.html',{
        'listaTemas':listaTemas
    })

def articulosPorTema(request,tema_id):
    tema = get_object_or_404(temaWiki, id=tema_id)
    articulos = articuloWiki.objects.filter(temaRelacionado=tema)
    return render(request, 'articulosPorTema.html',{
        'tema': tema, 
        'articulos': articulos
    })

def articulo(request, articulo_id):
    articulo = get_object_or_404(articuloWiki, id=articulo_id)

    return render(request, 'articulo.html',{
        'articulo':articulo
    })

def busquedaArticulos(request):

    query = request.GET.get('q', '')
    resultados = articuloWiki.objects.filter(titulo__icontains=query) if query else []

    return render(request, 'busquedaArticulos.html',{
        'query': query, 'resultados': resultados
    })