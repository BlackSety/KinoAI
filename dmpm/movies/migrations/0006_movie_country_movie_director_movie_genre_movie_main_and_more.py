# Generated by Django 4.0.5 on 2022-07-08 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_movie_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='country',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movie',
            name='director',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movie',
            name='genre',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movie',
            name='main',
            field=models.CharField(default=1, max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movie',
            name='producer',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movie',
            name='slogan',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
