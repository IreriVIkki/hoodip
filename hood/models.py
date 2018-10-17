from django.db import models
from django.contrib.auth.models import User
import math

# Create your models here.


class NeighbourHood(models.Model):
    admin = models.ForeignKey(
        User, null=True, on_delete=models.CASCADE, related_name='locations')
    name = models.CharField(max_length=50, null=True)
    location = models.CharField(max_length=50, null=True)
    occupants = models.IntegerField(null=True)
    address = models.IntegerField(null=True)

    @property
    def create_neigborhood(self, user):
        self.admin = user
        self.save()

    def __str__(self):
        return self.location


class Profile(models.Model):
    user = models.OneToOneField(
        User, null=True, on_delete=models.CASCADE, related_name='profile')
    user_name = models.CharField(max_length=50, null=True)
    profile_photo = models.ImageField(
        upload_to='images/', blank=True, default='dwf_profile.jpg')
    user_name = models.CharField(max_length=50, null=True)

    bio = models.TextField(blank=True)

    age = models.IntegerField(blank=True, null=True)
    phone = models.IntegerField(null=True)
    email = models.CharField(max_length=50, null=True)

    def save_profile(self, current_user):
        self.is_chief = False
        self.is_pro = False
        self.is_judge = False
        self.is_tribe = False
        self.user = current_user
        self.save()

    def __str__(self):
        return self.user_name
