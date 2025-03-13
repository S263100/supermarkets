from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], null=True,
                              blank=True)

    def __str__(self):
        return str(self.user)
