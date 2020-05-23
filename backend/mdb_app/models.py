from django.db import models
from django.forms import ModelChoiceField


# Create your models here.
class Article(models.Model):
    article_id = models.AutoField(primary_key=True)
    article_heading = models.CharField(max_length=250)
    article_body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False, blank=True)
    updated_at = models.DateTimeField(auto_now=True)


class Artista(models.Model):
    nome = models.CharField(max_length=50)
    cognome = models.CharField(max_length=50)
    src = models.ImageField(upload_to='uploads/%Y/%m/canzoni/artisti/', default='uploads/default.png')
    created_at = models.DateTimeField(auto_now_add=True, editable=False, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s %s' % (self.nome, self.cognome)

    class Meta:
        verbose_name_plural = "Artisti"


class Album(models.Model):
    titolo = models.CharField(max_length=50)
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE)
    pubblicazione = models.DateField()
    src = models.ImageField(upload_to='uploads/%Y/%m/canzoni/album/', default='uploads/default.png')
    created_at = models.DateTimeField(auto_now_add=True, editable=False, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Titolo Album: %s - Data Pubblicazione: %s' % (self.titolo, self.pubblicazione)


class Canzone(models.Model):
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, blank=True, null=True)
    titolo = models.CharField(max_length=50)
    src = models.ImageField(upload_to='uploads/%Y/%m/canzoni', default='uploads/default.png')
    created_at = models.DateTimeField(auto_now_add=True, editable=False, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s - Artista:%s' % (self.titolo, self.artista)

    class Meta:
            verbose_name_plural = "Canzoni"

class Genere(models.Model):
    nome = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True, editable=False, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % self.nome

    class Meta:
        verbose_name_plural = "Generi"

class Film(models.Model):
    titolo = models.CharField(max_length=50)
    pubblicazione = models.DateField()
    generi = models.ManyToManyField(Genere, blank=True)
    src = models.ImageField(upload_to='uploads/%Y/%m/film/', default='uploads/default.png')
    e_src = models.URLField(blank=True, null=True)
    tmdb_id = models.BigIntegerField(unique=True, blank=True, null=True)
    plot = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % self.titolo


class Attore(models.Model):
    nome = models.CharField(max_length=50)
    cognome = models.CharField(max_length=50)
    dob = models.DateField()
    tmdb_id = models.BigIntegerField(unique=True, blank=True, null=True)
    e_src = models.URLField(blank=True, null=True)
    src = models.ImageField(upload_to='uploads/%Y/%m/film/attori/', default='uploads/default.png')
    films = models.ManyToManyField(Film)
    created_at = models.DateTimeField(auto_now_add=True, editable=False, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s %s' % (self.nome, self.cognome)

    class Meta:
            verbose_name_plural = "Attori"

class Scrittore(models.Model):
    nome = models.CharField(max_length=50)
    cognome = models.CharField(max_length=50)
    dob = models.DateField()
    src = models.ImageField(upload_to='uploads/%Y/%m/libri/scrittori/', default='uploads/default.png')
    created_at = models.DateTimeField(auto_now_add=True, editable=False, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s %s' % (self.nome, self.cognome)

    class Meta:
            verbose_name_plural = "Scrittori"

class Libro(models.Model):
    titolo = models.CharField(max_length=50)
    pubblicazione = models.DateField()
    generi = models.ManyToManyField(Genere, blank=True)
    src = models.ImageField(upload_to='uploads/%Y/%m/libri/', default='uploads/default.png')
    e_src = models.URLField(blank=True, null=True)
    gbooks_id = models.CharField(max_length=50, unique=True, blank=True, null=True)
    plot = models.TextField(blank=True, null=True)
    scrittore = models.ForeignKey(Scrittore, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Titolo: %s - Scrittore: %s' % (self.titolo, self.scrittore)

    class Meta:
        verbose_name_plural = "Libri"