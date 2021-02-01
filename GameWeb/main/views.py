from django.contrib.auth.models import User
from django.views.generic import ListView, CreateView
from .models import Game
from django.contrib.auth.views import LoginView


class UserRegistrationView(CreateView):
    model = User


class GameListView(ListView):
    model = Game
    template_name = 'main/base.html'
    context_object_name = 'games'
