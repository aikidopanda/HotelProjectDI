from django.db import models
# from django.contrib.auth.models import User

class Type(models.Model):
    type_choice = (
        ('E', 'Economy'),
        ('B', 'Business'),
        ('L', 'Luxury'))
    types = models.CharField(max_length=50,
                    choices=type_choice,
                    default="E")
    def __str__(self):
        return f'{self.types}'

class Size(models.Model):
    size_choice = (
        ('1', 'One-person'),
        ('2', 'Two-person'),
        ('4', 'Four-person'))
    sizes = models.CharField(max_length=50,
                    choices=size_choice,
                    default="1")
    def __str__(self):
        return f'{self.sizes}'

class Room(models.Model):
    type = models.ForeignKey(Type, on_delete=models.DO_NOTHING)
    size = models.ForeignKey(Size, on_delete=models.DO_NOTHING)
    cost = models.FloatField()
    min_rent = models.IntegerField() # min period for which room can be rented
    animals_allowed = models.BooleanField(default=False)
    # price = models.IntegerField()
    def __str__(self) -> str:
        return f'{self.type}, {self.size}, {self.cost}, {self.min_rent}, {self.animals_allowed}'

class Review (models.Model):
    text = models.TextField()
    email  = models.EmailField(null=True, blank=True)
    def __str__(self) -> str:
        return f'{self.text}, {self.email}'

class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    # payment = models.BooleanField(default=False)
    def __str__(self):
        return f'{self.room}, {self.start_date}, {self.end_date}'

class ApartmentPhoto(models.Model):
    room = models.ForeignKey(Room,on_delete=models.DO_NOTHING, related_name='apartphoto')
    photo = models.ImageField(upload_to='media/')
    main_photo = models.BooleanField(default=False)
    def __str__(self):
        return f'{self.room}'