from django.urls import path
from . import views
from .views import (
    PhoneCreateView,
    PhoneDetailView,
    PhoneUpdateView,
    PhoneDeleteView
)

urlpatterns = [
    path('', views.home, name='home'),
    path('phone/<int:pk>/', PhoneDetailView.as_view(), name='phone-detail'),
    path('phone/new/', PhoneCreateView.as_view(), name='phone-create'),
    path('phone/<int:pk>/update/', PhoneUpdateView.as_view(), name='phone-update'),
    path('phone/<int:pk>/delete/', PhoneDeleteView.as_view(), name='phone-delete'),
]
