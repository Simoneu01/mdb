from rest_framework import viewsets
from .models import *
from .serializers import *


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArtistaViewSet(viewsets.ModelViewSet):
    queryset = Artista.objects.all()
    serializer_class = ArtistaSerializer


class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class CanzoneViewSet(viewsets.ModelViewSet):
    queryset = Canzone.objects.all()
    serializer_class = CanzoneSerializer


class GenereViewSet(viewsets.ModelViewSet):
    queryset = Genere.objects.all()
    serializer_class = GenereSerializer


class FilmViewSet(viewsets.ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer


class AttoreViewSet(viewsets.ModelViewSet):
    queryset = Attore.objects.all()
    serializer_class = AttoreSerializer


class ScrittoreViewSet(viewsets.ModelViewSet):
    queryset = Scrittore.objects.all()
    serializer_class = ScrittoreSerializer


class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer
