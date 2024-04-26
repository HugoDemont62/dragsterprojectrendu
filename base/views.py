from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Car, Bet, UserProfile
import random


@login_required
def home(request):
    Car.objects.update_or_create(name='voiture-bleu', defaults={'max_speed': 1000})
    Car.objects.update_or_create(name='voiture-rouge', defaults={'max_speed': random.randint(100, 130)})
    Car.objects.update_or_create(name='voiture-violette', defaults={'max_speed': random.randint(100, 130)})
    Car.objects.update_or_create(name='voiture-orange', defaults={'max_speed': random.randint(100, 130)})

    cars = Car.objects.all()
    user_bets = Bet.objects.filter(user_profile=request.user.userprofile)
    context = {'cars': cars, 'user_bets': user_bets, 'user_points': request.user.userprofile.points}
    return render(request, 'home.html', context)


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
    top_users = UserProfile.objects.order_by('-points')[:3]  # Get the top 3 users
    return render(request, 'classement.html', {'top_users': top_users})


def place_bet(request):
    if request.method == "POST":
        car = Car.objects.get(pk=request.POST['car'])
        points = int(request.POST['points'])
        user_profile = request.user.userprofile
        if user_profile.points >= points:
            user_profile.points -= points
            user_profile.save()
            Bet.objects.create(user_profile=user_profile, car=car, points=points)
    return render(request, "home.html",
                  {'cars': Car.objects.all(), 'bets': Bet.objects.filter(user_profile__user=request.user),
                   'user_points': request.user.userprofile.points})


def check_bet(request):
    if request.method == "POST":
        winning_car_id = request.POST['winning_car_id']
        print('winning_car_id', winning_car_id)
        user_bets = Bet.objects.filter(user_profile=request.user.userprofile)
        user_bet = user_bets[len(user_bets) - 1]
        print('user_bet', user_bet)
        if user_bet.car.id == int(winning_car_id):
            user_bet.user_profile.points += 2 * user_bet.points
            user_bet.user_profile.save()
            return JsonResponse({"message": "You won!"})

    return JsonResponse({"message": "You didn't bet."})
