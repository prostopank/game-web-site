# Generated by Django 3.1.5 on 2021-02-10 21:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_mustgames'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mustgames',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='get_games', to='main.game'),
        ),
    ]