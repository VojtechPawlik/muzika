from django.db import models

class Zanr(models.Model):
    nazev = models.CharField(max_length=100)

    def __str__(self):
        return self.nazev

class Interpret(models.Model):
    jmeno = models.CharField(max_length=100)
    popis = models.TextField(blank=True)
    zanr = models.ForeignKey(Zanr, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.jmeno

class Album(models.Model):
    nazev = models.CharField(max_length=200)
    interpret = models.ForeignKey(Interpret, on_delete=models.CASCADE)
    rok_vydani = models.PositiveIntegerField()
    pocet_skladeb = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.nazev} ({self.rok_vydani})"
