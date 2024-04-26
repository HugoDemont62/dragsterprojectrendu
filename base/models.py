from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='userprofile')
    points = models.IntegerField(default=1000)


class Car(models.Model):
    name = models.CharField(max_length=100, default='default_name')
    max_speed = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Bet(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    points = models.IntegerField()

    def __str__(self):
        return f'{self.user_profile.user.username} bet {self.points} on {self.car.name}'
