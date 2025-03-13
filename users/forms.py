from django import forms
from .models import Profile
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('phone_number', 'date_of_birth', 'gender')