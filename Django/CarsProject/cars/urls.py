from django.urls import path
from . import views

urlpatterns = [
    path('', views.cars, name='home'),
    path('ferrari', views.ferrari, name='ferrari')
]
