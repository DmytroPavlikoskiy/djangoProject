from django.db import models

class Users(models.Model):

    first_name = models.CharField('Імя', max_length=255)
    last_name = models.CharField('Прізвище', max_length=255)
    email = models.EmailField('Електронна Пошта')
    country = models.CharField('Країна', max_length=255)
    city = models.CharField('Місто', max_length=255)
    date_of_birth = models.DateField('Дата Народження')

    def __str__(self):
        return self.first_name