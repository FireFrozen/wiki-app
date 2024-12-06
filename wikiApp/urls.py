from . import views
from django.urls import path

app_name = 'wikiApp'

urlpatterns = [
    path('',views.index, name = 'homepage'),
    path('crearNuevoTema/',views.crearNuevoTema, name = 'crearNuevoTema'),
    path('crearNuevoArticulo/',views.crearNuevoArticulo, name = 'crearNuevoArticulo'),
    path('temas/<int:tema_id>/articulos/',views.articulosPorTema, name = 'articulosPorTema'),
    path('articulo/<int:articulo_id>/',views.articulo, name = 'articulo'),
    path('busquedaArticulos/',views.busquedaArticulos, name = 'busquedaArticulos'),
]