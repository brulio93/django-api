from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

# Create your models here.


class CustomUser(AbstractUser):
    objects = UserManager()


class Appointment(models.Model):
    appointment_id = models.IntegerField(blank=False, unique=True)
    appointment_date = models.DateTimeField(auto_now=False)
    appointment_user = CustomUser.username
