from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from .forms import ProfileForm, NoteForm
from .models import Profile, Note
from django.contrib import messages


def index(request):
    if request.user.is_authenticated:
        notes = Note.objects.all().filter(user=request.user).order_by('-pub_date')
        form = NoteForm()
        return render(request, "index.html", {"form": form, "notes": notes})
    else:
        return render(request, 'index.html')


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            login(request, user)
        return redirect("create_profile")
    else:
        form = UserCreationForm()
        return render(request, "registration/signup.html", {"form": form})


def create_profile(request):
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Your Profile has been saved!")
            return render(request, "index.html",)
    else:
        form = ProfileForm
        return render(request, "registration/create_profile.html", {"form": form})


def note(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            messages.success(request, "saved!")
            return redirect("index")
    else:
        pass

def delete_note(request, id):
    note = Note.objects.get(pk=id)
    note.delete()
    return redirect('index')

def details(request,id):
    note = Note.objects.get(pk=id)

    return render(request,'note.html',{'note':note} )