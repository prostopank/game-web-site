from django.core.management.base import BaseCommand
from ...models import Game, Genre, Platforms, ScreenShots
import requests


class Command(BaseCommand):
    def handle(self, *args, **options):
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/88.0.4324.104 Safari/537.36",
            "Client-ID": "qtc7d4yo7sm8k0a5vh23npv4fadlcz",
            "Authorization": "Bearer opdf898qp4f6usolymnkdt0zyo3uc6",
        }

        if Game.objects.filter(pk='2'):
            print('Yes')
        else:
            data = "fields name,first_release_date,rating,rating_count,genres.name,platforms.name,cover.url," \
                   "screenshots.url," \
                   "aggregated_rating,aggregated_rating_count,summary; where id = 2 & rating_count > 0 & aggregated_rating_count > " \
                   "0 & rating > 0 & aggregated_rating > 0; sort rating desc; limit 10;"
            responce = requests.post("https://api.igdb.com/v4/games", headers=headers, data=data)
            game = responce.json()
            print(game)