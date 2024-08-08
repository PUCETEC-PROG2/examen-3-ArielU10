from django.shortcuts import get_object_or_404, redirect, render

from .models import Artist, Album
from .forms import ArtistForm, AlbumForm

from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render (request, 'index.html')

def artistas(request):
    artistas = Artist.objects.all()
    context = {
        'artistas': artistas
    }
    return render (request, 'artistas.html', context)

def mostrar_artista(request, id):
    artista = Artist.objects.get(id=id)
    context = {
        'artista': artista
    }
    return render(request, 'artist_details.html', context)

@login_required
def add_artista(request):
    if request.method == 'POST':
        form = ArtistForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('album_manager:artistas')
    else:
        form = ArtistForm()
    
    return render(request, 'artista_form.html', {'form': form})

@login_required
def edit_artista(request, id):
    artista = get_object_or_404(Artist, pk = id)
    if request.method == 'POST':
        form = ArtistForm(request.POST, request.FILES, instance=artista)
        if form.is_valid():
            form.save()
            return redirect('album_manager:artistas')
    else:
        form = ArtistForm(instance=artista)
    
    return render(request, 'artista_form.html', {'form': form})

@login_required
def delete_artista(request, id):
    artista = get_object_or_404(Artist, pk = id)
    artista.delete()
    return redirect('album_manager:artistas')




def albums(request):
    albums = Album.objects.all()
    context = {
        'albums': albums
    }
    return render (request, 'albums.html', context)

def mostrar_album(request, id):
    album = Album.objects.get(id=id)
    context = {
        'album': album
    }
    return render(request, 'album_details.html', context)

@login_required
def add_album(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('album_manager:albums')
    else:
        form = AlbumForm()
    
    return render(request, 'album_form.html', {'form': form})

@login_required
def edit_album(request, id):
    album = get_object_or_404(Album, pk = id)
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES, instance=album)
        if form.is_valid():
            form.save()
            return redirect('album_manager:albums')
    else:
        form = AlbumForm(instance=album)
    
    return render(request, 'album_form.html', {'form': form})

@login_required
def delete_album(request, id):
    album = get_object_or_404(Album, pk = id)
    album.delete()
    return redirect('album_manager:albums')


class CustomLoginView(LoginView):
    template_name = 'login.html'
