from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
# Create your models here.




class Profile(models.Model):
    """Model definition for Profile."""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name = "profileUser")
    # Initialisation a la creation
    image = models.ImageField(upload_to="profile", blank=True)
    # date_add = models.DateTimeField(auto_now=False, auto_now_add=True)
    # date_upd = models.DateTimeField(auto_now=True, auto_now_add=False)
    # status = models.BooleanField(default=True)
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, created, **kwargs):
        instance.profileUser.save() ## prend le related_name qui le lie au model User

    # TODO: Define fields here

    class Meta:
        """Meta definition for Profile."""

        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'


class Tchater(models.Model):
    """Model definition for Tchater."""

    # TODO: Define fields here
    utilisateur = models.ForeignKey(Profile, related_name="profileTchat", on_delete=models.CASCADE)
    message = models.TextField()
    date_add = models.DateTimeField(auto_now=False, auto_now_add=True)
    status = models.BooleanField()

    class Meta:
        """Meta definition for Tchater."""

        verbose_name = 'Tchater'
        verbose_name_plural = 'Tchaters'
    


