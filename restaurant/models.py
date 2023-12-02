from django.db import models

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=256)
    no_of_guests = models.PositiveIntegerField()
    bookingDate = models.DateField()

    def __str__(self):
        return f"{self.name} - {self.bookingDate}"

class Menu(models.Model):
    title = models.CharField(max_length=256)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.title} : {str(self.price)}'
