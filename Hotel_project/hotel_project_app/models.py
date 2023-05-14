from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Room(models.Model):
    type_choice = (
        ('E', 'Economy'),
        ('B', 'Business'),
        ('L', 'Luxury'),
    )
    size_choice = (
        ('1', 'One-person'),
        ('2', 'Two-person'),
        ('4', 'Four-person'),
    )
    type = models.CharField(choices=type_choice)
    size = models.CharField(choices = size_choice)
    cost = models.FloatField()
    max_rent = models.IntegerField() # maximum period for which room can be rented
    guest = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    animals_allowed = models.BooleanField(default=False)


class Booking(models.Model):
    guest = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()




