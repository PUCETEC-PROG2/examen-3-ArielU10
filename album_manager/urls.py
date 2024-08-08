from django.urls import path
# Ingresar tus URLs de la app aquí

from . import views

app_name = 'album_manager'

urlpatterns = [
    path("", views.index, name="index"),
#artist
    path("artistas/", views.artistas, name="artistas"),
    path("add_artista/", views.add_artista, name='add_artista'),
    path("artistas/mostrar_artista/<int:id>/", views.mostrar_artista, name="mostrar_artista"),
    path("artistas/edit_artista/<int:id>/", views.edit_artista, name='edit_artista'),
    path("artistas/delete_artista/<int:id>/", views.delete_artista, name='delete_artista'),
#album
    path("albums/", views.albums, name="albums"),
    path("add_album/", views.add_album, name='add_album'),
    path("albums/mostrar_album/<int:id>/", views.mostrar_album, name="mostrar_album"),
    path("albums/edit_album/<int:id>/", views.edit_album, name='edit_album'),
    path("albums/delete_album/<int:id>/", views.delete_album, name='delete_album'),

    path("login/", views.CustomLoginView.as_view(), name='login'),
]
