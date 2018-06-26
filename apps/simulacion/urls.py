
from django.urls import path,re_path
from apps.simulacion import views
from django.contrib.auth.decorators import login_required
app_name = 'simulacion'
urlpatterns = [
    path('', views.index, name="index"),
	path('nuevo', (views.simulacion_view), name="new"),
	path('resultados', (views.simulacion_list), name="simulacion_listar"),
	re_path(r'^editar/(?P<id>\d+)/$', views.simulacion_edit, name="simulacion_editar"),

	]