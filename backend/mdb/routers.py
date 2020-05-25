from rest_framework import routers, serializers, viewsets
from mdb_app.viewsets import *
from .serializers import UserViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register('article', ArticleViewSet)
router.register('users', UserViewSet)
router.register('artista', ArtistaViewSet)
router.register('album', AlbumViewSet)
router.register('canzone', CanzoneViewSet)
router.register('genere', GenereViewSet)
router.register('film', FilmViewSet)
router.register('attore', AttoreViewSet)
router.register('autore', AutoreViewSet)
router.register('libro', LibroViewSet)
