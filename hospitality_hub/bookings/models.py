from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Course(models.Model):
    name = models.CharField()
    description = models.TextField()
    price = models.DecimalField()
    duration = models.IntegerField()
    last_update = models.DateTimeField()


class Booking(models.Model):        
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled'),
    ]

    user = models.ForeignKey()
    course = models.ForeignKey()
    booking_date = models.DateTimeField()
    start_date = models.DateField()
    status = models.CharField()
    notes = models.TextField()
