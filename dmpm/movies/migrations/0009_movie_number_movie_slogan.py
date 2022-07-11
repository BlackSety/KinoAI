# Generated by Django 4.0.5 on 2022-07-09 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0008_remove_movie_slogan'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='number',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movie',
            name='slogan',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]