from django.db import models

# Create your models here.
class Servicio(models.Model):
    id_servicio = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=False, null=False)
    precio = models.IntegerField(blank=False, null=False)
    foto = models.ImageField(upload_to='media')
    descripcion_lugar = models.TextField(max_length=500)

    def __str__(self):
        return self.descripcion_lugar

