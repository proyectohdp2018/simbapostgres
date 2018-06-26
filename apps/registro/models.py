from django.db import models

# Create your models here.
class usuario(models.Model):
	nombre = models.CharField(max_length=50, primary_key = True)
	profesion = models.CharField(max_length=50)
	correo = models.EmailField()
