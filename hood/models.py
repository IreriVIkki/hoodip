from django.db import models
from django.contrib.auth.models import User
import math

# Create your models here.


class NeighborHood(models.Model):
    CHOICES = (
        ('Mandera', ("Mandera")),
        ('Meru', ("Meru")),
        ('Migori', ("Migori")),
        ('Mombasa', ("Mombasa")),
        ('Muranga', ("Muranga")),
        ('Nairobi', ("Nairobi")),
        ('Nakuru', ("Nakuru")),
        ('Nandi', ("Nandi")),
        ('Nyamira', ("Nyamira")),
        ('Nyeri', ("Nyeri")),
    )
    admin = models.ForeignKey(
        User, null=True, on_delete=models.CASCADE, related_name='locations')
    location = models.CharField(max_length=50, choices=CHOICES, null=True)
    name = models.CharField(max_length=50, null=True)
    occupants = models.IntegerField(null=True)
    residents = models.ManyToManyField(
        User, related_name='residents')
    address = models.IntegerField(null=True)

    @property
    def population(self):
        population = self.occupants + len(self.residents.all())
        return population

    @property
    def businesses(self):
        businesses = Business.objects.filter(located_at=self)
        return businesses

    @property
    def notifications(self):
        notifications = Notification.objects.filter(hood=self)
        return notifications

    @classmethod
    def new_hood(cls):
        return cls.objects.last()

    def create_neigborhood(self, hood, admin):
        hood.admin = admin
        hood.save()

    def delete_neigborhood(self):
        self.delete()

    @classmethod
    def find_neigborhood(cls, neigborhood_id):
        return cls.objects.filter(pk=neigborhood_id)

    def update_neighborhood(self):
        self.save()

    def update_occupants(self, occupants):
        self.occupants = occupants
        self.save()

    @classmethod
    def all_hoods(cls):
        return cls.objects.all()

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(
        User, null=True, on_delete=models.CASCADE, related_name='profile')
    user_name = models.CharField(max_length=50, null=True)
    profile_photo = models.ImageField(
        upload_to='images/', blank=True, default='dwf_profile.jpg')
    neighborhood = models.ForeignKey(
        NeighborHood, on_delete=models.CASCADE, null=True)
    phone = models.IntegerField(null=True)
    email = models.CharField(max_length=50, null=True)

    # @classmethod
    # def new_user(cls):
    #     return cls.objects.last()

    @classmethod
    def create_profile(cls, user):
        cls.objects.create(user=user, user_name=user.username)

    @property
    def businesses(self):
        businesses = Business.objects.filter(owner=self)
        return businesses

    def save_profile(self, current_user):
        self.user = current_user
        self.save()

    def leave_hood(self, hood_id, user):
        hood = NeighborHood.objects.get(pk=hood_id)
        hood.residents.remove(user)
        self.neighborhood = None
        self.save()

    def join_hood(self, hood_id, user):
        hood = NeighborHood.objects.get(pk=hood_id)
        hood.residents.add(user)
        self.neighborhood = hood
        self.save()

    def __str__(self):
        return self.user_name


class Business(models.Model):
    name = models.CharField(max_length=100,)
    owner = models.ForeignKey(
        User, related_name='businesses', null=True, on_delete=models.CASCADE)
    located_at = models.ForeignKey(
        NeighborHood, null=True, on_delete=models.CASCADE, related_name='businesses')
    description = models.TextField(null=True)
    email = models.CharField(max_length=50, null=True)
    link = models.CharField(max_length=50, null=True)

    def create_business(self, owner, locale):
        self.owner = owner
        self.located_at = locale
        self.save()

    def delete_business(self):
        self.delete()

    @classmethod
    def find_business(cls, business_id):
        return cls.objects.get(pk=business_id)

    @classmethod
    def search_businesses(cls, search_term):
        dec = cls.objects.filter(description__icontains=search_term)
        nam = cls.objects.filter(name__icontains=search_term)
        print(list(dec) + list(nam))
        return list(dec) + list(nam)

    @classmethod
    def find_user_businesses(cls, user):
        return cls.objects.filter(owner=user)

    def update_business(self):
        self.save()

    @classmethod
    def get_bs_by_id(cls, id):
        return cls.objects.get(pk=id)

    @classmethod
    def new_business(cls):
        return cls.objects.last()

    def __str__(self):
        return self.name


class Notification(models.Model):
    author = models.ForeignKey(
        User, null=True, related_name='notifications', on_delete=models.CASCADE)
    hood = models.ForeignKey(
        NeighborHood, null=True, on_delete=models.CASCADE, related_name='notifications')
    message = models.TextField()

    def save_notification(self, author, hood):
        self.author = author
        self.hood = hood
        self.save()

    def delete_notification(self):
        self.delete()


class Amenities(models.Model):
    CHOICES = (
        ('Mandera', ("Mandera")),
        ('Meru', ("Meru")),
        ('Migori', ("Migori")),
        ('Mombasa', ("Mombasa")),
    )
    institution = models.CharField(
        max_length=50, choices=CHOICES)
    name = models.CharField(max_length=100)
    hood = models.ForeignKey(NeighborHood, null=True,
                             related_name='institutions', on_delete=models.CASCADE)

    def save_amenitiy(self, hood):
        self.hood = hood
        self.save()

    def __str__(self):
        return self.name
