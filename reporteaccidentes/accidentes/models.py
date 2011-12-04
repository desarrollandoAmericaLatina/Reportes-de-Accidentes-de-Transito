from django.db import models

# Create your models here.
class Accidente(models.Model):
	calle = models.CharField(max_length=200)
	cruce = models.CharField(max_length=200)
	tipo = models.CharField(max_length=200)
	year = models.CharField(max_length=200)
	nombre_calle = models.CharField(max_length=200)
	nombre_cruce = models.CharField(max_length=200)
	esquina = models.CharField(max_length=200)
	latititud =  models.CharField(max_length=200)
	longitude = models.CharField(max_length=200)
