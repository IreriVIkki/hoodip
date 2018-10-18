from django.db import models
from django.contrib.auth.models import User
import math

# Create your models here.


class NeighborHood(models.Model):
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

    @classmethod
    def delete_neigborhood(cls, hood_name):
        cls.objects.filter(name=hood_name).delete()

    @classmethod
    def find_neigborhood(cls, neigborhood_id):
        return cls.objects.filter(pk=neigborhood_id)

    def update_neighborhood(self):
        self.save()

    @property
    def update_occupants(self, occupants):
        self.occupants = occupants
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
    neighborhood = models.ForeignKey(
        NeighborHood, on_delete=models.CASCADE, null=True)
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


class Business(models.Model):
    name = models.CharField(max_length=100,)
    owner = models.ForeignKey(
        User, related_name='owner', null=True, on_delete=models.CASCADE)
    located_at = models.ForeignKey(
        NeighborHood, null=True, on_delete=models.CASCADE)
    email = models.CharField(max_length=50)

    def create_business(self, owner, locale):
        self.owner = owner
        self.located_at = locale
        self.save()

    def delete_business(self):
        self.delete()

    @classmethod
    def find_business(cls, business_id):
        return cls.objects.get(pk=business_id)

    def update_business(self):
        self.save()

    def __str__(self):
        return self.name
