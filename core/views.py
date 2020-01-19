from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from .forms import ProfileForm
from .models import Profile
from django.contrib import messages


def index(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('profile_create')
    else:
        form = UserCreationForm()
        return render(request, 'registration/signup.html', {'form':form})

def create_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your Profile has been saved!')
            return render(request, 'index.html', )
    else:
        form = ProfileForm
        return render(request, 'registration/create_profile.html', {'form':form})