from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from apps.registro.forms import RegistroForm
from django.contrib.auth.decorators import login_required


# Create your views here.

class RegistroUsuario(CreateView):
	model = User
	templete_name = "registro/registrar.html"
	form_class = RegistroForm
	success_url = '/ingresar'

@login_required()
def welcome(request):
	return render(request, 'registro/welcome.html')