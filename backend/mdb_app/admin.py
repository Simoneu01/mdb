from django.contrib import admin
from .models import *


class BasicAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'created_at', 'updated_at')


class AlbumAdmin(admin.ModelAdmin):
    list_display = ('titolo', 'artista', 'pubblicazione', 'created_at', 'updated_at')


class CanzoneAdmin(admin.ModelAdmin):
    list_display = ('titolo', 'artista', 'album', 'created_at', 'updated_at')


class FilmAdmin(admin.ModelAdmin):
    list_display = ('titolo', 'pubblicazione', 'created_at', 'updated_at')


class AttoreAdmin(admin.ModelAdmin):
    list_display = ('titolo', 'pubblicazione', 'created_at', 'updated_at')


class LibroAdmin(admin.ModelAdmin):
    list_display = ('titolo', 'pubblicazione', 'scrittore', 'created_at', 'updated_at')


# Register your models here.
admin.site.register(Article)
admin.site.register(Artista, BasicAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Canzone, CanzoneAdmin)
admin.site.register(Genere, BasicAdmin)
admin.site.register(Film, FilmAdmin)
admin.site.register(Attore, BasicAdmin)
admin.site.register(Scrittore, BasicAdmin)
admin.site.register(Libro, LibroAdmin)
