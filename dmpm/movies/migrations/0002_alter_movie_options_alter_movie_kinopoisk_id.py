# Generated by Django 4.0.5 on 2022-07-02 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='movie',
            options={'verbose_name': 'фильм', 'verbose_name_plural': 'фильмы'},
        ),
        migrations.AlterField(
            model_name='movie',
            name='kinopoisk_id',
            field=models.CharField(max_length=1000),
        ),
    ]
