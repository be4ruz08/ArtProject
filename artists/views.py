from django.shortcuts import render, get_object_or_404
from .models import Artist
from gallery.models import ArtWork


def artist_list(request):
    artists = Artist.objects.all()
    return render(request, 'artists/artist_list.html', {'artists': artists})


def artist_detail(request, artist_id):
    artist = get_object_or_404(Artist, id=artist_id)
    artworks = ArtWork.objects.filter(artist=artist)
    return render(request, 'artists/artist_detail.html', {'artist': artist, 'artworks': artworks})
