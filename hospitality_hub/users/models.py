from django.db import models
from django.contrib.auth.models import User

 
# Create your models here.

class UserProfile(models.model):
    user = models.OneToOneField()
    phone =  models.CharField()
    address = models.TextField
    email = models.EmailField()


UserProfile()