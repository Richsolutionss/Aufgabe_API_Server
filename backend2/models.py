
from django.db import models

class Server(models.Model) :
    title = models.CharField(max_length=256)
    description = models.TextField(blank=True)
    preis = models.IntegerField()
    produkt_url = models.URLField(blank=True)

    hersteller = models.ForeignKey('Hersteller',
                                   on_delete=models.CASCADE)
    lager = models.ForeignKey('Lager',
                                   on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Hersteller(models.Model) :
    name = models.CharField(max_length=256)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Lager(models.Model) :
    name = models.CharField(max_length=256)
    ort = models.CharField(max_length=256)

    def __str__(self):
        return  self.name