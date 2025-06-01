from django.db import models

class Zanr(models.Model):
    nazev = models.CharField(max_length=100)

    def __str__(self):
        return self.nazev

class Interpret(models.Model):
    jmeno = models.CharField(max_length=100)

    def __str__(self):
        return self.jmeno

class Album(models.Model):
    nazev = models.CharField(max_length=200)
    interpret = models.ForeignKey(Interpret, on_delete=models.CASCADE)
    zanr = models.ForeignKey(Zanr, on_delete=models.SET_NULL, null=True)
    rok = models.PositiveIntegerField()

    def __str__(self):
        return self.nazev
