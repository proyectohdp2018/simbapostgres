from django import forms
from apps.simulacion.models import SimulacionCostoProduccion

class SimulacionForm(forms.ModelForm):
	
	class Meta:
		model = SimulacionCostoProduccion

		fields = [

			
			'profundidad',
			'sistemaDrenaje',
			'plagas',
			'deshoje',
			'embolse',
			'lvlMar',
			'temperatura',
			'luminosidad',
			'fechaSim',
			'pluviosidad',
			'tipoSuelo',
			'fosforo',
			'potasio',
			'magnesio',
			'calcio',
			'ph',
			'zinc',
			'boro',

			


		]
		labels = {

			
			'profundidad': 'Profundidad (en metros)',
			'sistemaDrenaje': 'Sistema de drenaje (si o no)',
			'plagas': 'Plagas ( si o no )',
			'deshoje': 'Deshoje (periodico o no)',
			'embolse': 'Embolse ( si o no )',
			'lvlMar': 'Nivel del mar(en metros)',
			'temperatura': 'Temperatura(grados celcios)',
			'luminosidad': 'luminosidad(horas de luz por planta al dia)',
			'densidadSiembra': 'Densidad de siembra',
			'fechaSim': 'Fecha de Simulacion (ingresar año-mes-dia)',
			
			'pluviosidad': 'Pluviosidad por planta (Mensual en ml)',
			'tipoSuelo' : 'Tipo de suelo (arido, arcilloso o franco)',
			'fosforo': 'Nivel de fosforo del suelo',
			'potasio':	'Nivel de potasio del suelo',
			'magnesio': 'Nivel de magnesio en el suelo',
			'calcio': 'Nivel de Calcio  del suelo',
			'ph': 'Nivel de PH del suelo',
			'zinc': 'Nivel de Zinc del suelo',
			'boro':'boro',
			



		}
		widgets = {


			

			'profundidad': forms.NumberInput(attrs={'class': 'form-control'}),
			'sistemaDrenaje': forms.TextInput(attrs={'class': 'form-control'}),
			'plagas': forms.TextInput(attrs={'class': 'form-control'}),
			'deshoje': forms.TextInput(attrs={'class': 'form-control'}),
			'embolse': forms.TextInput(attrs={'class': 'form-control'}),
			'lvlMar': forms.NumberInput(attrs={'class': 'form-control'}),
			'temperatura': forms.NumberInput(attrs={'class': 'form-control'}),
			'luminosidad': forms.NumberInput(attrs={'class': 'form-control'}),
			'densidadSiembra': forms.NumberInput(attrs={'class': 'form-control'}),
			'fechaSim': forms.TextInput(attrs={'class': 'form-control'}),
			'pluviosidad': forms.NumberInput(attrs={'class': 'form-control'}),
			'tipoSuelo' : forms.TextInput(attrs={'class': 'form-control'}),
			'fosforo':forms.NumberInput(attrs={'class': 'form-control'}),
			'potasio':forms.NumberInput(attrs={'class': 'form-control'}),
			'magnesio':forms.NumberInput(attrs={'class': 'form-control'}),
			'calcio':forms.NumberInput(attrs={'class': 'form-control'}),
			'ph':forms.NumberInput(attrs={'class': 'form-control'}),
			'zinc':forms.NumberInput(attrs={'class': 'form-control'}),
			'boro':forms.NumberInput(attrs={'class': 'form-control'}),




		}



