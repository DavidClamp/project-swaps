from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

# Trigger: When a User is created...
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        # Action: Create a matching Profile
        Profile.objects.create(user=instance)

# Trigger: When a User is saved...
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    # Action: Save the matching Profile
    instance.profile.save()