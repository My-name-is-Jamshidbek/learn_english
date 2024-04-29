# models.py
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    country = models.CharField(max_length=100, blank=True)
    bio = models.TextField(blank=True, null=True)
    total_score = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.first_name} {self.last_name}"


class StaffProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    country = models.CharField(max_length=200, blank=True)
    bio = models.TextField(blank=True, null=True)
    education = models.TextField(blank=True, null=True)
    experience = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.first_name} {self.last_name}"


# views.py or elsewhere
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created and not instance.is_staff:
        # Ensuring all required fields are populated
        if hasattr(instance, 'userprofile'):
            StaffProfile.objects.create(
                user=instance,
                first_name=instance.first_name or '',
                last_name=instance.last_name or '',
                date_of_birth=instance.date_of_birth or None,  # Handle missing dates gracefully
                country=instance.country or '',
            )
        else:
            UserProfile.objects.create(
                user=instance,
                first_name=instance.first_name or '',
                last_name=instance.last_name or '',
                date_of_birth=instance.date_of_birth or None,  # Handle missing dates gracefully
                country=instance.country or '',
            )


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if hasattr(instance, 'staffprofile'):
        instance.staffprofile.save()
    else:
        instance.userprofile.save()
