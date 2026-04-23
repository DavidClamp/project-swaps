from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Uses get_or_create to prevent IntegrityErrors during Allauth signup.
    """
    if created:
        # This handles the "duplicate key" bug by checking if profile exists first
        Profile.objects.get_or_create(user=instance)
  
    # Safely save the profile if it exists
    if hasattr(instance, 'profile'):
        instance.profile.save()
