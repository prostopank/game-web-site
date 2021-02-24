import django_filters
from django import forms
from django_filters.widgets import RangeWidget, SuffixedMultiWidget

from .models import Game, Genre, Platforms


class GameFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.TextInput(
            attrs={'class': 'form-control ml-2 mr-4', 'style': 'text-align:center; width: 160px; height:30px'}))
    rating = django_filters.RangeFilter(widget=RangeWidget(
        attrs={'class': 'ml-2',
               'style': 'border:1px solid rgb(180,166,166,.60); border-radius:3px;width: 80px; height:30px'}))
    genre = django_filters.ChoiceFilter(choices=[(genre.pk, genre) for genre in Genre.objects.all(
    )], widget=forms.Select(attrs={'class': 'form-control ml-2 mr-4', 'style': 'width: 160px; height:30px'}))
    platforms = django_filters.ChoiceFilter(choices=[(platform.pk, platform) for platform in Platforms.objects.all(
    )], widget=forms.Select(attrs={'class': 'form-control ml-2 mr-5', 'style': 'width: 160px; height:30px'}))
