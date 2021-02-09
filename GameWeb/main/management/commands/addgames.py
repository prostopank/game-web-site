from django.core.management.base import BaseCommand
from datetime import datetime
import requests
import time
from ...models import Game, Genre, Platforms, ScreenShots


class Command(BaseCommand):
    def handle(self, *args, **options):
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/88.0.4324.104 Safari/537.36",
            "Client-ID": "qtc7d4yo7sm8k0a5vh23npv4fadlcz",
            "Authorization": "Bearer opdf898qp4f6usolymnkdt0zyo3uc6",
        }
        l = 0
        for step in range(1, 130000, 500):
            data = "fields name,first_release_date,rating,rating_count,genres.name,platforms.name,cover.url," \
                   "screenshots.url," \
                   "aggregated_rating,aggregated_rating_count,summary; where rating_count > 0 & aggregated_rating_count > " \
                   "0 & rating > 0 & aggregated_rating > 0 & id > {}; sort id asc; limit 500;".format(step)

            responce = requests.post("https://api.igdb.com/v4/games", headers=headers, data=data)
            games = responce.json()

            for game in games:
                if Game.objects.filter(pk=game['id']):
                    pass
                else:
                    if 'genres' in game:
                        for genre in game['genres']:
                            if Genre.objects.filter(pk=genre['id']):
                                pass
                            else:
                                Genre.objects.create(
                                    id=genre['id'],
                                    name=genre['name'],
                                )
                    else:
                        pass
                    if 'platforms' in game:
                        for platform in game['platforms']:
                            if Platforms.objects.filter(pk=platform['id']):
                                pass
                            else:
                                Platforms.objects.create(
                                    id=platform['id'],
                                    name=platform['name'],
                                )
                    else:
                        pass
                    if 'summary' in game:
                        if 'cover' in game:
                            cover = game['cover']['url'].replace('t_thumb', 't_cover_big')
                        else:
                            cover = ''
                        temp_game = Game.objects.create(
                            id=game['id'],
                            name=game['name'],
                            first_release_date=datetime.utcfromtimestamp(game['first_release_date']).strftime(
                                '%Y-%m-%d %H:%M:%S'),
                            rating=game['rating'],
                            rating_count=game['rating_count'],
                            aggregated_rating=game['aggregated_rating'],
                            aggregated_rating_count=game['aggregated_rating_count'],
                            summary=game['summary'],
                            cover=cover,
                        )
                        if 'genres' in game:
                            for genre in game['genres']:
                                temp_game.genre.add(genre['id'])
                        if 'platforms' in game:
                            for platform in game['platforms']:
                                temp_game.platforms.add(platform['id'])
                        temp_game.save()

                        if 'screenshots' in game:
                            for screenshot in game['screenshots']:
                                ScreenShots.objects.create(
                                    game=Game.objects.get(id=game['id']),
                                    url=screenshot['url'].replace('t_thumb', 't_cover_big'),
                                )
                        else:
                            pass

            time.sleep(1)
            l += 1

            print(str(l) + " of 260")
