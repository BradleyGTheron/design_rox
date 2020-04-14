from django.urls import path, include
from . import views

app_name = 'print'

urlpatterns = [
    path('<int:id>/<str:slug>', views.print_detail, name='print_detail')
]
