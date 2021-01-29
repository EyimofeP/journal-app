from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import ListView


from .models import Diary

class DiaryListView(LoginRequiredMixin, ListView):
    model = Diary
    template_name = "core/home.html"
    context_object_name = "journals"
    login_url = "login"
