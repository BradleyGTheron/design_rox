"""design_rox URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf .urls.static import static
import print.views

admin.site.site_header = 'Designs By Rox Dicky Admin'
admin.site.site_title = 'Designs By Rox Dicky Admin'
admin.site.index_title = 'Designs By Rox Dicky Administration'



urlpatterns = [
    path('', print.views.home, name = 'home'),
    path('cart/', include('cart.urls', namespace='cart')),
    path('print/', include('print.urls', namespace='print')),
    path('photo/', include('photo.urls')),
    path('wedding/', include('wedding.urls')),
    path('party/', include('party.urls')),
    path('business/', include('business.urls')),
    path('kid/', include('kid.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
