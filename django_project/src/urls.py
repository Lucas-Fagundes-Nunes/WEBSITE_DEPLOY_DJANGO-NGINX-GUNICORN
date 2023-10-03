# myapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Outras URLs do aplicativo...
    path('', views.home, name='home'),
    path('teste/', views.teste, name='teste'),
]
