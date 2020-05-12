from django.db import models


# Create your models here.
class Article(models.Model):
    article_id = models.AutoField(primary_key=True)
    article_heading = models.CharField(max_length=250)
    article_body = models.TextField()


class Artista(models.Model):
    nome = models.CharField(max_length=50)
    cognome = models.CharField(max_length=50)
    foto = models.ImageField()


class Album(models.Model):
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE)
    nome = models.CharField(max_length=50)
    pubblicazione = models.DateField()
    copertina = models.ImageField()


class Canzone(models.Model):
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    titolo = models.CharField(max_length=50)
    copertina = models.ImageField()


class Genere(models.Model):
    nome = models.CharField(max_length=50)


class Film(models.Model):
    titolo = models.CharField(max_length=50)
    pubblicazione = models.DateField()
    generi = models.ManyToManyField(Genere)


class Attore(models.Model):
    nome = models.CharField(max_length=50)
    cognome = models.CharField(max_length=50)
    dob = models.DateField()
    foto = models.ImageField()
    films = models.ManyToManyField(Film)


class Scrittore(models.Model):
    nome = models.CharField(max_length=50)
    cognome = models.CharField(max_length=50)
    dob = models.DateField()
    foto = models.ImageField()

class Libro(models.Model):
    titolo = models.CharField(max_length=50)
    pubblicazione = models.DateField()
    generi = models.ManyToManyField(Genere)
    scrittore = models.ForeignKey(Scrittore, on_delete=models.CASCADE)
