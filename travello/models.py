from django.db import models

# Create your models here.
class Destinations(models.Model):
# poprzez migration rekordy dodawane sa jako naglowki tabel do bazy danych
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)

class Attractions(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    city = models.CharField(max_length=100, default='miasto')
    street = models.CharField(max_length=100, default='ulica')
    voivodeship = models.CharField(max_length=100, default='wojewodztwo')
    price = models.IntegerField(default='0')
    desc = models.TextField(default='')
    img = models.ImageField(upload_to='pics')
    duration = models.IntegerField(default=0)
    num_people = models.IntegerField(default=1)
    offer = models.BooleanField(default=False)

class History(models.Model):
    user = models.CharField(max_length=100)
    name = models.CharField(max_length=100, default='brak nazwy')
    city = models.CharField(max_length=100, default='miasto')
    voivodeship = models.CharField(max_length=100, default='brak danych')
    date = models.DateField()
