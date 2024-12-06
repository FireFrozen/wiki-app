from django.db import models

# Create your models here.
class temaWiki(models.Model):
    nombre = models.CharField(max_length=128, null=True, blank=True)
    descripcion = models.CharField(max_length=512, null=True, blank=True)

class articuloWiki(models.Model):
    titulo = models.CharField(max_length=128, null=True, blank=True)
    contenido = models.CharField(max_length=1024, null=True, blank=True)
    temaRelacionado = models.ForeignKey(
        temaWiki, 
        on_delete=models.CASCADE, 
        related_name='articulos'
    )