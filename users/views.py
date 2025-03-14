import profile
from django.contrib.messages import success
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from .forms import CustomUserChangeForm, ProfileForm, Profile
from .models import Profile
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.models import User, Group


# Create your views here.
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect("home")
    else:
            form = UserCreationForm()
    return render(request, "users/register.html",{ "form": form})

class password_change_view(PasswordChangeView):
    template_name = 'users/change_password.html'
    success_url = reverse_lazy('users:password_change_done')

@login_required
def password_change_done_view(request):
    return render(request, 'users/password_change_done.html')


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect("home")
    else:
        form = AuthenticationForm
    return render(request, "users/login.html", {"form": form})

def profile_view(request):
    profile_instance = Profile.objects.get_or_create(user=request.user)

    is_admin = request.user.groups.filter(name="Admin").exists()
    return render(request, "users/account.html", {"user": request.user,
     "profile": profile_instance, 'is_admin': is_admin})

def profile_edit_view(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    if request.method == "POST":
        user_form = CustomUserChangeForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect("home")
    else:
            user_form = CustomUserChangeForm(instance=request.user)
            profile_form = ProfileForm(instance=request.user.profile)
    return render(request, "users/edit_profile.html",{ "user_form": user_form,
    "profile_form": profile_form})


def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("home")
