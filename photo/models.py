from django.db import models

class PhotoGallery(models.Model):
    image = models.ImageField('Gallery Image', upload_to='photos/')
    image_tn = models.ImageField('Thumbnail Image', upload_to='photos/')
    title = models.CharField('Print Title', max_length=50)
    enabled = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Gallery Photo'
        verbose_name_plural = 'Gallery Photos'

    def __str__(self):
        return self.title
