from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from decimal import Decimal


# Create your models here.
class Booking(models.Model):
    ID = models.PositiveIntegerField(
        primary_key = True,
        unique = True,
    )
    Name = models.CharField(max_length=255)
    No_of_guests = models.IntegerField(
    )
    BookingDate = models.DateTimeField()

    def __str__(self):
        return str(self.ID) + " " +  str(self.Name)




class Menu(models.Model):
    ID = models.PositiveIntegerField(
        primary_key = True,
        unique = True,
    )
    Title = models.CharField(max_length=255)
    Price = models.DecimalField(max_digits=10, decimal_places=2, validators=
                                [
                                    MinValueValidator(Decimal('0.01'))
                                ])
    Inventory = models.PositiveIntegerField()

    def __str__(self):
        return str(self.ID) + " " +  str(self.Title)




    
    
