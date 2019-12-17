from django.db import models

# Create your models here.
class Book(models.Model):
    book_name = models.CharField(max_length=32)
    book_price = models.FloatField(default=1)

class Game(models.Model):
    game_name = models.CharField(max_length=32)
    game_price = models.FloatField(default=1)


class Movie(models.Model):
    movie_name = models.CharField(max_length=32)
    movie_price = models.FloatField(default=1)

class User(models.Model):
    user_name = models.CharField(max_length=32,unique=True)
    user_password = models.CharField(max_length=256)
