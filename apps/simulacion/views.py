from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.simulacion.forms import SimulacionForm
from apps.simulacion.models import SimulacionCostoProduccion
from apps.produccion.models import Produccion,Cosecha
from apps.registro.models import usuario
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User


# Create your views here.
@login_required(login_url ='/ingresar')
def index(request):
	return render(request,'simulacion/index.html')
	

@login_required(login_url ='/ingresar')
def simulacion_view (request):
	objetoCosecha= ()
	if request.method == 'POST':
		if 'btnFormSim' in request.POST:
			usuario1 = ()
			usuario1 =  request.user
			usuariosim = ()
			
			tipoSuelo = request.POST.get('tipoSuelo')
			profundidad = float(request.POST.get('profundidad'))
			sistemaDrenaje = request.POST.get('sistemaDrenaje')
			plagas =  request.POST.get('plagas')
			deshoje = request.POST.get('deshoje')
			embolse =  request.POST.get('embolse')
			lvlMar =float(request.POST.get('lvlMar'))
			temperatura =float( request.POST.get('temperatura'))
			pluviosidad = float(request.POST.get('pluviosidad'))
			luminosidad = float(request.POST.get('luminosidad'))
			
			fechaSim= request.POST.get('fechaSim')
			fosforo =float(request.POST.get('fosforo'))
			potasio =float(request.POST.get('potasio'))
			calcio =float(request.POST.get('calcio'))
			magnesio =float(request.POST.get('magnesio'))
			boro =float(request.POST.get('boro'))
			zinc =float(request.POST.get('zinc'))
			ph =float(request.POST.get('ph'))
			



			if tipoSuelo == 'arido' :
				puntajeSuelo = 2
			elif tipoSuelo == 'arcilloso':
				puntajeSuelo = 5
			elif tipoSuelo == 'franco':
				puntajeSuelo == 15

			if profundidad >1.2 and profundidad< 1.5 :
				puntajeProfu = 15
			else:
				puntajeProfu = 5

			if sistemaDrenaje == 'si':
				puntajeDrenaje = 15
			else:
				puntajeDrenaje  = 2

			if plagas == 'si' :
				puntajePlagas = 2
			else:
				puntajePlagas = 15

			if deshoje == 'periodico':
				puntajeDeshoje = 15
			elif deshoje == 'no':
				puntajeDeshoje = 2
			else:
				puntajeDeshoje = 5

			if lvlMar > 500 and lvlMar < 1000:
				puntajeMar = 15
			else:
				puntajeMar = 5

			if temperatura == 27:
				puntajeTemp = 15
			elif temperatura > 21 and temperatura < 30:
				puntajeTemp = 10
			else:
			 	puntajeTemp = 2

			if pluviosidad > 101 and pluviosidad < 180:
			 	puntajePluvi = 15
			elif pluviosidad < 100:
			 	puntajePluvi = 5
			else:
			 	puntajePluvi = 10

			if luminosidad > 4 and luminosidad < 6 :
			 	puntajeLumi = 15
			else:
			 	puntajeLumi = 5

			if fosforo >20:
			 	puntajeFosforo = 5
			elif fosforo < 10:
			 	puntajeFosforo = 5
			else:
			 	puntajeFosforo = 15

			if potasio>0.5:
				puntajePotasio = 5
			elif potasio <0.5:
				puntajePotasio = 5
			else:
				puntajePotasio = 15

			if calcio > 6:
				puntajeCalcio = 5
			elif calcio < 3:
				puntajeCalcio = 2
			else:
				puntajeCalcio = 15

			if magnesio > 3:
				puntajeMagnesio= 5
			elif magnesio < 1:
				puntajeMagnesio= 2
			else:
				puntajeMagnesio = 15

			if boro > 0.7:
				puntajeBoro =5
			elif boro < 0.2:
				puntajeBoro = 2
			else:
				puntajeBoro = 15

			if zinc > 15:
				puntajeZinc = 5
			elif zinc < 3:
				puntajeZinc = 2
			else:
				puntajeZinc = 15

			if ph> 6.5:
				puntajePh = 5
			elif ph < 5:
				puntajePh = 5
			else:
				puntajePh = 15

			if embolse == ' si':
				puntajeEmbolse = 15
			else:
				puntajeEmbolse = 5

			puntajeSim = 0
			puntajeSim = (puntajeEmbolse+puntajeSuelo+puntajeProfu+puntajeDrenaje+puntajePlagas+puntajeDeshoje+puntajeMar+puntajeTemp+
				puntajePluvi+puntajeLumi+puntajeFosforo+puntajePotasio+puntajeCalcio+puntajeMagnesio+puntajeBoro+puntajeZinc+puntajePh)

			objetoSimulacion  = SimulacionCostoProduccion(usuarioSim = usuario1, tipoSuelo=tipoSuelo, sistemaDrenaje = sistemaDrenaje,
				plagas = plagas, deshoje = deshoje, embolse =embolse , lvlMar = lvlMar, temperatura = temperatura,
				pluviosidad = pluviosidad, luminosidad = luminosidad, fechaSim = fechaSim, puntajeSimu = puntajeSim, profundidad = profundidad, fosforo = fosforo, potasio = potasio,calcio = calcio, magnesio = magnesio,
				boro = boro, zinc = zinc, ph = ph)
			objetoSimulacion.save()

			if puntajeSim > 240 and puntajeSim <270:
				objetoCosecha = Cosecha.objects.get(id = 3)

			if puntajeSim > 210 and puntajeSim <240:
				objetoCosecha = Cosecha.objects.get(id = 4)

			if puntajeSim > 180 and puntajeSim <210:
				objetoCosecha = Cosecha.objects.get(id = 5)

			if puntajeSim > 120 and puntajeSim <180:
				objetoCosecha = Cosecha.objects.get(id = 6)

			if puntajeSim > 90 and puntajeSim <120:
				objetoCosecha = Cosecha.objects.get(id = 7)

			if puntajeSim > 60 and puntajeSim <90:
				objetoCosecha = Cosecha.objects.get(id = 8)

			if puntajeSim < 60:
				objetoCosecha = Cosecha.objects.get(id = 9)


			form = SimulacionForm(request.POST)
		
	else:
		
		form= SimulacionForm()
	contexto = {
	'form' : form,
	'objetoCosecha' : objetoCosecha,
	}
	#print(objetoCosecha.grosorTallo)
	return render(request, 'simulacion/simulacion_form.html', {'contexto':contexto})

@login_required(login_url='/ingresar')
def simulacion_list(request):
	simulacion = SimulacionCostoProduccion.objects.filter(usuarioSim =request.user)
	contexto = {'simulaciones': simulacion}

	return render(request, 'simulacion/simulacion_list.html', contexto)
@login_required(login_url ='/ingresar')

def simulacion_edit(request,id):
	objetoCosecha= ()
	simulacion = SimulacionCostoProduccion.objects.get(id = id)
	if request.method=='GET':
	 	form = SimulacionForm(instance = simulacion)
	elif request.method == 'POST':
	 	form = SimulacionForm(request.POST, instance = simulacion)
	 	if form.is_valid():
	 		form.save()
	 	if 'btnFormSim' in request.POST:
	 		usuarioSim=()
	 		usuario1 = request.user


	 		tipoSuelo = request.POST.get('tipoSuelo')
	 		profundidad = float(request.POST.get('profundidad'))
	 		sistemaDrenaje = request.POST.get('sistemaDrenaje')
	 		plagas =  request.POST.get('plagas')
	 		deshoje = request.POST.get('deshoje')
	 		embolse =  request.POST.get('embolse')
	 		lvlMar =float(request.POST.get('lvlMar'))
	 		temperatura =float( request.POST.get('temperatura'))
	 		pluviosidad = float(request.POST.get('pluviosidad'))
	 		luminosidad = float(request.POST.get('luminosidad'))
	 		fechaSim= request.POST.get('fechaSim')
	 		fosforo =float(request.POST.get('fosforo'))
	 		potasio =float(request.POST.get('potasio'))
	 		calcio =float(request.POST.get('calcio'))
	 		magnesio =float(request.POST.get('magnesio'))
	 		boro =float(request.POST.get('boro'))
	 		zinc =float(request.POST.get('zinc'))
	 		ph =float(request.POST.get('ph'))



	 		
	 		if tipoSuelo == 'arido':
	 			puntajeSuelo = 2

	 		elif tipoSuelo == 'arcilloso':
	 			puntajeSuelo==10

	 		elif tipoSuelo  == 'franco':
	 			puntajeSuelo = 15
	 		else:
	 			puntajeSuelo = 3

	 		if profundidad >1.2 and profundidad< 1.5 :
	 			puntajeProfu = 15
	 		else:
	 			puntajeProfu = 5

	 		if sistemaDrenaje == 'si':
	 			puntajeDrenaje = 15
	 		else:
	 			puntajeDrenaje = 2

	 		if plagas == 'si' :
	 			puntajePlagas = 2
	 		else:
	 			puntajePlagas = 15

	 		if deshoje == 'periodico':
	 			puntajeDeshoje = 15
	 		elif deshoje == 'no':
	 			puntajeDeshoje = 2

	 		if lvlMar > 500 and lvlMar < 1000:
	 			puntajeMar = 15
	 		else:
	 			puntajeMar = 5

	 		if temperatura == 27:
	 			puntajeTemp = 15
	 		elif temperatura > 21 and temperatura < 30:
	 			puntajeTemp = 10

	 		else:
	 			puntajeTemp = 2

	 		if pluviosidad > 101 and pluviosidad < 180:
	 			puntajePluvi = 15
	 		elif pluviosidad < 100:
	 			puntajePluvi = 5
	 		else:
	 			puntajePluvi = 10

	 		if luminosidad > 4 and luminosidad < 6 :
	 			puntajeLumi = 15
	 		else:
	 			puntajeLumi =5 

	 		if fosforo >20:
	 			puntajeFosforo = 5
	 		elif fosforo < 10:
	 			puntajeFosforo = 5
	 		else:
	 			puntajeFosforo = 15

	 		if potasio > 0.5:
	 			puntajePotasio = 5
	 		elif potasio < 0.5:
	 			puntajePotasio = 5
	 		else:
	 			puntajePotasio = 15

	 		if calcio > 6:
	 			puntajeCalcio = 5
	 		elif calcio < 3:
	 			puntajeCalcio =2 
	 		else:
	 			puntajeCalcio = 15

	 		if magnesio > 3:
	 			puntajeMagnesio = 5
	 		if magnesio <1:
	 			puntajeMagnesio = 2
	 		else: 
	 			puntajeMagnesio = 15

	 		if boro > 0.7:
	 			puntajeBoro = 5
	 		elif boro < 0.2 :
	 			puntajeBoro = 2
	 		else: 
	 			puntajeBoro = 15

	 		if zinc > 15:
	 			puntajeZinc = 5
	 		elif zinc < 3:
	 			puntajeZinc =2 
	 		else:
	 			puntajeZinc = 15

	 		if ph> 6.5:
	 			puntajePh = 5
	 		elif ph < 5:
	 			puntajePh = 5
	 		else:
	 			puntajePh = 15
	 		
	 		if embolse == 'si':
	 			puntajeEmbolse = 15
	 		elif embolse == 'no':
	 			puntajeEmbolse = 10
	 		else:
	 			puntajeEmbolse = 2


	 		puntajeSim=0
	 		
	 		puntajeSim =(puntajeEmbolse+puntajeSuelo+puntajeProfu+puntajeDrenaje+puntajePlagas+puntajeDeshoje+puntajeMar+puntajeTemp+
	 			puntajePluvi+puntajeLumi+puntajeFosforo+puntajePotasio+puntajeCalcio+puntajeMagnesio+puntajeBoro+puntajeZinc+puntajePh)

	 		objetoSimulacion  = SimulacionCostoProduccion(usuarioSim = usuario1, tipoSuelo=tipoSuelo, sistemaDrenaje = sistemaDrenaje,
	 			plagas = plagas, deshoje = deshoje, embolse =embolse , lvlMar = lvlMar, temperatura = temperatura,
	 			pluviosidad = pluviosidad, luminosidad = luminosidad, fechaSim = fechaSim, puntajeSimu = puntajeSim, profundidad = profundidad, fosforo = fosforo, potasio = potasio,calcio = calcio, magnesio = magnesio,
	 			boro = boro, zinc = zinc, ph = ph)


	 		if puntajeSim > 240 and puntajeSim <270:
	 			objetoCosecha = Cosecha.objects.get(id = 3)

	 		if puntajeSim > 210 and puntajeSim <240:
	 			objetoCosecha = Cosecha.objects.get(id = 4)

	 		if puntajeSim > 180 and puntajeSim <210:
	 			objetoCosecha = Cosecha.objects.get(id = 5)

	 		if puntajeSim > 120 and puntajeSim <180:
	 			objetoCosecha = Cosecha.objects.get(id = 6)

	 		if puntajeSim > 90 and puntajeSim <120:
	 			objetoCosecha = Cosecha.objects.get(id = 7)

	 		if puntajeSim > 60 and puntajeSim <90:
	 			objetoCosecha = Cosecha.objects.get(id = 8)

	 		if puntajeSim < 60:
	 			objetoCosecha = Cosecha.objects.get(id = 9)
				






	 		form = SimulacionForm(request.POST)
	else:
		form = SimulacionForm()
	contexto = {
		'form': form,
		'objetoCosecha':objetoCosecha,
		}
	return render(request, 'simulacion/simulacion_form.html', {'contexto':contexto})




          		
	 	#return redirect('/simulacion/resultados')
	#return render (request, 'simulacion/simulacion_form.html', {'form':form})










