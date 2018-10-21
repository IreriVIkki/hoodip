from django.shortcuts import HttpResponse, render, redirect, get_object_or_404, reverse, get_list_or_404
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import mail_admins
from django.contrib.auth.models import User
from django.contrib import auth, messages
from .forms import *
from .models import *
import datetime

# Create your views here.


def home(request):
    if request.user.is_authenticated == False:
        return redirect('login')
    user = request.user
    user_bs = Business.find_user_businesses(user)
    hoods = NeighborHood.all_hoods()
    form = HoodForm()
    bs_form = BusinessForm()
    if request.method == 'POST':
        bs_form = BusinessForm(request.POST)
        form = HoodForm(request.POST)
        admin = request.user
        if form.is_valid():
            print('here')
            new_hood = form.save()
            new_hood.create_neigborhood(new_hood, admin)
            user.profile.join_hood(new_hood.id, admin)
        if bs_form.is_valid():
            print('here')
            new_bs = bs_form.save()
            new_bs.create_business(user, user.profile.neighborhood)
        return redirect('home')

    context = {
        'user': user,
        'user_bs': user_bs,
        'hoods': hoods,
        'form': form,
        'bs_form': bs_form
    }
    return render(request, 'index.html', context)


def leave_hood(request, hood_id):
    user = request.user
    user.profile.leave_hood(hood_id, user)
    return redirect('home')


def delete_business(request, bs_id):
    bs = Business.get_bs_by_id(bs_id)
    bs.delete_business()
    return redirect('home')


def join_hood(request, hood_id):
    user = request.user
    user.profile.join_hood(hood_id, user)
    return redirect('home')


def edit_profile(request, id, username):
    context = {
        'user': request.user
    }
    return render(request, 'profile.html', context)


def login(request):
    if request.user.is_authenticated():
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            # correct username and password login the user
            auth.login(request, user)
            return redirect('home')

        else:
            messages.error(request, 'Error wrong username/password')

    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('login')


def signup(request):
    if request.method == 'POST':
        form = MyRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.create_profile(user)
            print(user.profile.user_name)
            return redirect('login')

    form = MyRegistrationForm()

    context = {
        'form': form
    }
    return render(request, 'register.html', context)
