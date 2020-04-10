from django.urls import path
from . import views

urlpatterns = [
    path('', views.business, name = 'business'),
]
