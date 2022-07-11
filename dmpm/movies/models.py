from django.db import models


class Movie(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(max_length=5000)
    image = models.ImageField(upload_to='movie')
    magnet_link = models.TextField(max_length=1000)
    country = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    producer = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    main = models.CharField(max_length=300)

    class Meta:
        verbose_name = 'фильм'
        verbose_name_plural = 'фильмы'

    def __str__(self):
        return self.name
