from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.simulacion.forms import SimulacionForm
from apps.simulacion.models import SimulacionCostoProduccion
from apps.produccion.models import Cosecha
from django.contrib.auth.decorators import login_required

from apps.produccion.models import Cosecha
# Create your views here.\
@login_required(login_url ='/ingresar')
def calculos(request):
	return render(request,'base/produccion/index.html')
