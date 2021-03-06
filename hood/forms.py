from django import forms
# fill in custom user info then save it
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *


class MyRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(MyRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        user.save()

        return user


class HoodForm(forms.ModelForm):

    class Meta:
        model = NeighborHood
        exclude = ['admin', 'residents']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user', 'neighborhood']


class BusinessForm(forms.ModelForm):

    class Meta:
        model = Business
        exclude = ['owner', 'located_at']


class NotificationForm(forms.ModelForm):

    class Meta:
        model = Notification
        exclude = ['author', 'hood']
