import django_filters
from django import forms
from django_filters.widgets import RangeWidget, SuffixedMultiWidget

from .models import Game, Genre, Platforms


class GameFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'text-align:center'}))
    rating = django_filters.RangeFilter(widget=RangeWidget(
        attrs={'size': '6%', 'style': 'border:1px solid rgb(180,166,166,.60); border-radius:3px;'}))
    genre = django_filters.ChoiceFilter(choices=[(genre.pk, genre) for genre in Genre.objects.all(
    )], widget=forms.Select(attrs={'class': 'form-control'}))
    platforms = django_filters.ChoiceFilter(choices=[(platform.pk, platform) for platform in Platforms.objects.all(
    )], widget=forms.Select(attrs={'class': 'form-control'}))
