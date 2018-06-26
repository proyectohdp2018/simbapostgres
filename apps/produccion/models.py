from django.db import models

# Create your models here.
class Cosecha(models.Model):
	alturaPlanta = models.DecimalField(max_digits = 5, decimal_places = 2)
	grosorTallo = models.DecimalField(max_digits = 5, decimal_places = 2)
	numeroHojas = models.DecimalField(max_digits = 5, decimal_places = 2)
	pesoRacimo = models.DecimalField(max_digits = 5, decimal_places = 2)
	costoHectarea = models.DecimalField(max_digits = 5, decimal_places = 2,null = True)
	kgCosechados = models.IntegerField(null = True)
	precioKg =  models.DecimalField(max_digits = 5, decimal_places = 2,null = True)
	utilidadEsperada = models.IntegerField(null = True)

class Produccion(models.Model):
	costoHectarea = models.DecimalField(max_digits = 5, decimal_places = 2)
	kgCosechados = models.DecimalField(max_digits = 5, decimal_places = 2)
	precioKg =  models.DecimalField(max_digits = 5, decimal_places = 2)
	utilidadEsperada = models.DecimalField(max_digits = 5, decimal_places = 2)
	cosecha = models.OneToOneField(Cosecha,null = True, blank = True, on_delete = models.CASCADE)
