from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, DetailView

from .filters import GameFilter
from .forms import RegisterUserForm
from .models import Game, MustGames


class RegisterUserView(CreateView):
    model = User
    template_name = 'registration/register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('games')


def show_all_games_page(request):
    context = {}
    filtered_game = GameFilter(request.GET, queryset=Game.objects.all())
    context['filtered_game'] = filtered_game
    paginated_filtered_person = Paginator(filtered_game.qs, 12)
    page_number = request.GET.get('page')
    game_page_obj = paginated_filtered_person.get_page(page_number)
    context['game_page_obj'] = game_page_obj
    if request.user.is_authenticated:
        context['must_games'] = MustGames.objects.filter(user=request.user)
    else:
        context['must_games'] = None
    return render(request, 'main/games.html', context=context)


class DeleteOfMustGamesView(View):
    def get(self, request, *args, **kwargs):
        user = request.user.id
        game = kwargs.get('pk')
        if MustGames.objects.filter(user_id=user, game_id=game):
            instance = MustGames.objects.filter(user_id=user, game_id=game)
            instance.delete()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class GameDetailView(DetailView):
    model = Game
    template_name = 'main/detail_game.html'
    context_object_name = 'get_game'


def show_must_games_page(request):
    context = {}
    must_game = MustGames.objects.filter(user=request.user)
    context['must_games_user'] = must_game
    return render(request, 'main/must_games.html', context=context)


class AddToMustView(View):
    def get(self, request, *args, **kwargs):
        user = request.user.id
        game = kwargs.get('pk')
        if MustGames.objects.filter(user_id=user, game_id=game):
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            MustGames.objects.create(
                user_id=user, game_id=game
            )
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class ProfileView(ListView):
    model = User
    template_name = 'main/profile.html'
