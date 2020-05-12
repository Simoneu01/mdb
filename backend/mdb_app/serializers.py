from rest_framework import serializers
from .models import *


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'


class ArtistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artista
        fields = '__all__'


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'


class CanzoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Canzone
        fields = '__all__'


class GenereSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genere
        fields = '__all__'


class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = '__all__'


class AttoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attore
        fields = '__all__'


class ScrittoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scrittore
        fields = '__all__'


class LibroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libro
        fields = '__all__'
