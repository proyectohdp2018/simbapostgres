from django.urls import path,re_path
from apps.produccion import views
urlpatterns = [
    path('', views.calculos, name="index"),
    re_path(r'^calculos/(?P<id>\d+)/$', views.calculos, name="produccion_calculos"),
    ]