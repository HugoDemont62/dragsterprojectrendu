from django.db import models


# Create your models here.
class Car(models.Model):
    name = models.CharField(max_length=100, default='default_name')
    max_speed = models.IntegerField(default=0)

    def __str__(self):
        return self.name
