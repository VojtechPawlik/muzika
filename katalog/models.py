from django.db import models

class Zanr(models.Model):
    nazev = models.CharField(max_length=100)
    popis = models.TextField(blank=True)
    popularita = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.nazev


class Interpret(models.Model):
    jmeno = models.CharField(max_length=100)
    popis = models.TextField(blank=True)
    narozeni = models.PositiveIntegerField(null=True, blank=True)
    zeme_puvodu = models.CharField(max_length=50, blank=True)
    obrazek = models.ImageField(upload_to='interpreti/', blank=True, null=True)
    zanry = models.ManyToManyField(Zanr, blank=True)

    def __str__(self):
        return self.jmeno


class Album(models.Model):
    nazev = models.CharField(max_length=200)
    interpret = models.ForeignKey('Interpret', on_delete=models.CASCADE)
    zanr = models.ForeignKey(Zanr, on_delete=models.SET_NULL, null=True)
    rok_vydanni = models.PositiveIntegerField()
    obrazek = models.ImageField(upload_to='alba/', blank=True, null=True)

    def __str__(self):
        return self.nazev
