from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from future_apps.models import Profile

def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

def save_profile(sender, instance, **kwargs):
    instance.profile.save()