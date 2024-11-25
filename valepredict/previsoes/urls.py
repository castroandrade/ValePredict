from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'previsao'

urlpatterns = [
    path('', views.home, name='home'),
    path('calcular/', views.calcular_previsao, name='calcular_previsao'),
    path('login/', auth_views.LoginView.as_view(template_name='previsoes/login.html'), name='login'),
    path('register/', views.register, name='register'),
]