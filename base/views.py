from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Car
import random


@login_required
def home(request):
    Car.objects.update_or_create(name='voiture-bleu', defaults={'max_speed': random.randint(100, 130)})
    Car.objects.update_or_create(name='voiture-rouge', defaults={'max_speed': random.randint(100, 130)})
    Car.objects.update_or_create(name='voiture-violette', defaults={'max_speed': random.randint(100, 130)})
    Car.objects.update_or_create(name='voiture-orange', defaults={'max_speed': random.randint(100, 130)})

    cars = Car.objects.all()

    return render(request, 'home.html', {'cars': cars})


def authView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect("base:login")
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})


def regleView(request):
    return render(request, "regle.html")


def classementView(request):
    return render(request, "classement.html")
