from django.db import models
from django.forms import ModelChoiceField


# Create your models here.
class Article(models.Model):
    article_id = models.AutoField(primary_key=True)
    article_heading = models.CharField(max_length=250)
    article_body = models.TextField()


class Artista(models.Model):
    nome = models.CharField(max_length=50)
    cognome = models.CharField(max_length=50)
    foto = models.ImageField(upload_to='uploads/%Y/%m/canzoni/artisti/', blank=True, null=True)

    def __str__(self):
        return '%s %s' % (self.nome, self.cognome)


class Album(models.Model):
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE)
    nome = models.CharField(max_length=50)
    pubblicazione = models.DateField()
    copertina = models.ImageField(upload_to='uploads/%Y/%m/canzoni/album/', blank=True, null=True)

    def __str__(self):
        return 'Titolo Album: %s - Data Pubblicazione: %s' % (self.nome, self.pubblicazione)

class Canzone(models.Model):
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    titolo = models.CharField(max_length=50)
    copertina = models.ImageField(upload_to='uploads/%Y/%m/canzoni', blank=True, null=True)

    def __str__(self):
        return '%s:%s' % (self.titolo, self.album)

class Genere(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return '%s' % (self.nome)


class Film(models.Model):
    titolo = models.CharField(max_length=50)
    pubblicazione = models.DateField()
    generi = models.ManyToManyField(Genere)
    copertina = models.ImageField(upload_to='uploads/%Y/%m/film/', blank=True, null=True)

    def __str__(self):
        return '%s' % (self.titolo)


class Attore(models.Model):
    nome = models.CharField(max_length=50)
    cognome = models.CharField(max_length=50)
    dob = models.DateField()
    foto = models.ImageField(upload_to='uploads/%Y/%m/film/attori/', blank=True, null=True)
    films = models.ManyToManyField(Film)

    def __str__(self):
        return '%s %s' % (self.nome, self.cognome)


class Scrittore(models.Model):
    nome = models.CharField(max_length=50)
    cognome = models.CharField(max_length=50)
    dob = models.DateField()
    foto = models.ImageField(upload_to='uploads/%Y/%m/libri/scrittori/', blank=True, null=True)

    def __str__(self):
        return '%s %s' % (self.nome, self.cognome)

class Libro(models.Model):
    titolo = models.CharField(max_length=50)
    pubblicazione = models.DateField()
    generi = models.ManyToManyField(Genere)
    copertina = models.ImageField(upload_to='uploads/%Y/%m/libri/', blank=True, null=True)
    scrittore = models.ForeignKey(Scrittore, on_delete=models.CASCADE)

    def __str__(self):
        return 'Titolo: %s - Scrittore: %s' % (self.titolo, self.scrittore)
