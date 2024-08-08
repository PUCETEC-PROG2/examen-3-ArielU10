from django import forms
from .models import Album, Artist

class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class' : 'form-control'}),
            'country': forms.TextInput(attrs={'class' : 'form-control'}),
        }

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class' : 'form-control'}),
            'release_year': forms.NumberInput(attrs={'class' : 'form-control'}),
            'genre': forms.TextInput(attrs={'class' : 'form-control'}),
            'artist': forms.Select(attrs={'class' : 'form-control'}),
            'front_page': forms.ClearableFileInput(attrs={'class' : 'form-control'}),
        }