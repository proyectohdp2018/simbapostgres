from django.db import models
from apps.registro.models import usuario
from apps.produccion.models import Cosecha
from django.contrib.auth.models import User

# Create your models here.
class SimulacionCostoProduccion (models.Model):
	tipoSuelo = models.CharField(max_length = 20)
	fosforo = models.DecimalField(max_digits = 5, decimal_places = 2,null = True)
	potasio = models.DecimalField(max_digits = 5, decimal_places = 2,null = True)
	calcio =models.DecimalField(max_digits = 5, decimal_places = 2,null = True) 
	magnesio =models.DecimalField(max_digits = 5, decimal_places = 2,null = True)
	boro = models.DecimalField(max_digits = 5, decimal_places = 2,null = True)
	zinc =models.DecimalField(max_digits = 5, decimal_places = 2,null = True)
	ph=models.DecimalField(max_digits = 5, decimal_places = 2,null = True)
	profundidad = models.DecimalField(max_digits = 5, decimal_places = 2)
	sistemaDrenaje = models.CharField(max_length = 20)
	plagas =  models.CharField(max_length = 20)
	deshoje =  models.CharField(max_length = 20)
	embolse =  models.CharField(max_length = 20)
	lvlMar = models.DecimalField(max_digits = 5, decimal_places = 2)
	temperatura = models.DecimalField(max_digits = 5, decimal_places = 2)
	pluviosidad = models.DecimalField(max_digits = 5, decimal_places = 2)
	luminosidad = models.DecimalField(max_digits = 5, decimal_places = 2)
	usuarioSim = models.ForeignKey(User,null = True, blank = True, on_delete = models.CASCADE)
	cosecha = models.ForeignKey(Cosecha,null = True, blank = True, on_delete = models.CASCADE)
	fechaSim= models.DateField(null = True)
	puntajeSimu = models.IntegerField(null = True)
	numHectareas=models.DecimalField(max_digits = 5, decimal_places = 4,null=True)
	numPlantas=models.IntegerField(null = True)

