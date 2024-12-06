from .models import temaWiki

def lista_temas(request):
    lista_temas = temaWiki.objects.all()
    return {'lista_temas': lista_temas}