from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.shortcuts import render

from .forms import CustomUserCreationForm, CustomUserUpdateForm

class SignUp(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

def userProfile(request):
    user = request.user
    form = CustomUserUpdateForm(instance=user)
    frontend = {"form": form}

    if request.method == "POST":
        form = CustomUserUpdateForm(request.POST, instance=user)
        if form.is_valid:
            form.save()
    return render(request, "registration/user-update.html", frontend)
