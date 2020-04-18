from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, blank=True)
    surname = models.CharField(max_length=50, blank=True)
    street_address = models.CharField(max_length=150, blank=True)
    suburb = models.CharField(max_length=50, blank=True)
    postal_code = models.CharField(max_length=5, blank=True)
    city = models.CharField(max_length=30, blank=True)
    contact_number = models.CharField(max_length=12, blank=True)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.surname)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
