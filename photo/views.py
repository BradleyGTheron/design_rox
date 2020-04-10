from django.shortcuts import render
from .models import PhotoGallery

def photo_gallery(request):
    photo_gallery = PhotoGallery.objects.filter(enabled = True)
    return render(request, 'photo/photo_gallery.html', {'photo_gallery': photo_gallery })
