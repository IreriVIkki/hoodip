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
    searched_posts = None
    caption = None
    user_bs = Business.find_user_businesses(user)
    hoods = NeighborHood.all_hoods()
    form = HoodForm()
    bs_form = BusinessForm()
    if 'post' in request.GET and request.GET['post']:
        # get the data from the search input field
        search_term = request.GET.get('post')
        searched_posts = Business.search_businesses(search_term)
        caption = f'Search results for {search_term}'

        if len(searched_posts) == 0:
            caption = f'Results for {search_term} Found'
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
    print(searched_posts)
    context = {
        'posts': searched_posts,
        'caption': caption,
        'user': user,
        'user_bs': user_bs,
        'hoods': hoods,
        'form': form,
        'bs_form': bs_form
    }
    return render(request, 'index.html', context)


# def search_results(request):
#     # check if the input field exists and that ic contains data
#     if 'post' in request.GET and request.GET['post']:
#         # get the data from the search input field
#         explore_posts = Post.all_posts()
#         search_term = request.GET.get('post')
#         searched_posts = Post.filter_by_search_term(search_term)
#         print(search_term)
#         caption = f'Search results for {search_term}'

#         if len(searched_posts) == 0:
#             caption = f'Results for {search_term} Found'
#         search_context = {
#             'posts': searched_posts,
#             'explore_posts': explore_posts,
#             'caption': caption,
#         }
#         return render(request, 'search.html', search_context)
#     else:
#         explore_posts = Post.all_posts()
#         search_context = {
#             'explore_posts': explore_posts,
#             'caption': 'Matches found for your search!! Discover More Posts'
#         }
#         return render(request, 'search.html', search_context)


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
