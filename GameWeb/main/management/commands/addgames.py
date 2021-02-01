from django.core.management.base import BaseCommand
from datetime import datetime
import requests

from ...models import Game, Genre, Platforms, ScreenShots


class Command(BaseCommand):
    def handle(self, *args, **options):
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/88.0.4324.104 Safari/537.36",
            "Client-ID": "qtc7d4yo7sm8k0a5vh23npv4fadlcz",
            "Authorization": "Bearer opdf898qp4f6usolymnkdt0zyo3uc6",
        }
        data = "fields name,first_release_date,rating,rating_count,genres.name,platforms.name,cover.url," \
               "screenshots.url," \
               "aggregated_rating,aggregated_rating_count,summary; where rating_count > 0 & aggregated_rating_count > " \
               "0 & rating > 0 & aggregated_rating > 0; sort rating desc; limit 500;"

        responce = requests.post("https://api.igdb.com/v4/games", headers=headers, data=data)
        games = responce.json()

        for game in games:
            if Game.objects.filter(pk=game['id']):
                pass
            else:
                if 'summary' in game:
                    Game.objects.create(
                        id=game['id'],
                        name=game['name'],
                        first_release_date=datetime.utcfromtimestamp(game['first_release_date']).strftime(
                            '%Y-%m-%d %H:%M:%S'),
                        rating=game['rating'],
                        rating_count=game['rating_count'],
                        aggregated_rating=game['aggregated_rating'],
                        aggregated_rating_count=game['aggregated_rating_count'],
                        summary=game['summary'],
                        cover=game['cover']['url'].replace('t_thumb', 't_cover_big'),
                    )
                    if 'genres' in game:
                        for genre in game['genres']:
                            Genre.objects.create(
                                game=Game.objects.get(id=game['id']),
                                name=genre['name'],
                            )
                    else:
                        pass
                    if 'platforms' in game:
                        for platform in game['platforms']:
                            Platforms.objects.create(
                                game=Game.objects.get(id=game['id']),
                                name=platform['name'],
                            )
                    else:
                        pass
                    if 'screenshots' in game:
                        for screenshot in game['screenshots']:
                            ScreenShots.objects.create(
                                game=Game.objects.get(id=game['id']),
                                url=screenshot['url'].replace('t_thumb', 't_cover_big'),
                            )
                    else:
                        pass
