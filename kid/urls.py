from django.urls import path
from . import views

urlpatterns = [
    path('', views.kid, name = 'kid'),
]
