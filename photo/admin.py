from django.contrib import admin
from .models import PhotoGallery

class PhotoGalleryAdmin(admin.ModelAdmin):
    list_display = ['title','image_tn','enabled']
    list_editable = ['enabled']
    list_per_page = 20

admin.site.register(PhotoGallery, PhotoGalleryAdmin)

# Register your models here.
