from django.urls import path,re_path
from apps.registro import views
from apps.registro.views import RegistroUsuario
from apps.simulacion.views import index
from django.contrib.auth.decorators import login_required
urlpatterns = [
    path('', RegistroUsuario.as_view(template_name = "registro/registrar.html"), name = "registrar"),
    


    ]

