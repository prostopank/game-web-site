from django.db import models


class Game(models.Model):
    id = models.IntegerField(primary_key=True, null=False)
    name = models.CharField(null=False, max_length=150, verbose_name='name')
    first_release_date = models.DateTimeField(auto_now=False, verbose_name='first_release_date')
    rating = models.FloatField(null=True, verbose_name='rating')
    rating_count = models.IntegerField(null=True, verbose_name='rating_count')
    aggregated_rating = models.FloatField(null=True, verbose_name='aggregated_rating')
    aggregated_rating_count = models.IntegerField(null=True, verbose_name='aggregated_rating_count')
    summary = models.TextField(verbose_name='summary')
    cover = models.URLField(null=True, verbose_name='cover')

    def __str__(self):
        return self.name


class Genre(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='game_genre')
    name = models.CharField(max_length=100, null=False, verbose_name='name')

    def __str__(self):
        return self.name


class Platforms(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='game_platforms')
    name = models.CharField(max_length=100, null=False, verbose_name='Name')

    def __str__(self):
        return self.name


class ScreenShots(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='game_screenshots')
    url = models.URLField(verbose_name="Url")

    def __str__(self):
        return self.url
