from django.urls import path
from . import views

urlpatterns = [
    path('', views.party, name = 'party'),
]
