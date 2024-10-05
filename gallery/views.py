from django.shortcuts import render, get_object_or_404
from .models import ArtWork


def artwork_list(request):
    artworks = ArtWork.objects.all()
    return render(request, 'gallery/artwork_list.html', {'artworks': artworks})


def artwork_detail(request, artwork_id):
    artwork = get_object_or_404(ArtWork, id=artwork_id)
    return render(request, 'gallery/artwork_detail.html', {'artwork': artwork})
