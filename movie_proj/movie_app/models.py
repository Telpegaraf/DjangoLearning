from django.db import models
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.

class Director(models.Model):
    first_name = models.CharField(max_length=100, default='Quentin')
    last_name = models.CharField(max_length=100, default='Tarantino')
    director_email = models.CharField(max_length=100, default='sugar@test.tu')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class DressingRoom(models.Model):
    floor = models.IntegerField()
    number = models.IntegerField()

    def __str__(self):
        return f"Этаж {self.floor}, комната {self.number}"


class Actor(models.Model):
    Male = 'M'
    Female = 'F'
    GENDERS = [
        (Male, 'Male'),
        (Female, 'Female'),
    ]

    first_name = models.CharField(max_length=100, default='Quentin')
    last_name = models.CharField(max_length=100, default='Tarantino')
    gender = models.CharField(max_length=1, choices=GENDERS, null=True)
    dressing = models.OneToOneField(DressingRoom, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        if self.gender == self.Male:
            return f"Актёр {self.first_name} {self.last_name}"
        else:
            return f" Актриса {self.first_name} {self.last_name}"


class Movie(models.Model):
    EUR = 'EUR'
    USD = 'USD'
    RUB = 'RUB'
    CURRENCY_CHOICES = [
        (EUR, 'Euro'),
        (USD, 'Dollar'),
        (RUB, 'Rubles'),
    ]

    name = models.CharField(max_length=40)
    rating = models.IntegerField()
    year = models.IntegerField(null=True, blank=True) # blank=True - можно сохранять пустое поле
    budget = models.IntegerField(default=1000000)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default='RUB') # Выбор из изначений
    slug = models.SlugField(default='', null=False, db_index=True)
    director = models.ForeignKey(Director, on_delete=models.PROTECT, null=True) # Добавить связь с другим классом
    # (PROTECT не дает удалить связь, если она назначена, CASCADE удаляет обе связи,
    # SET_NULL удаляет только часть связи)
    actors = models.ManyToManyField(Actor)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(args,kwargs)

    def get_url(self):
        return reverse('movie_detail', args=[self.slug])

    def __str__(self):
        return f"{self.name} - {self.rating}"

# from movie_app.models import Movie
