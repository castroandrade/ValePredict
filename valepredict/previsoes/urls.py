from django.urls import path
from . import views

app_name = 'previsao'

urlpatterns = [
    path('', views.home, name='home'),
    path('calcular/', views.calcular_previsao, name='calcular_previsao'),
]