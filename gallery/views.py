from django.views.generic import ListView, DetailView
from .models import ArtWork


class ArtWorkListView(ListView):
    model = ArtWork
    template_name = 'gallery/artwork_list.html'
    context_object_name = 'artworks'


class ArtWorkDetailView(DetailView):
    model = ArtWork
    template_name = 'gallery/artwork_detail.html'
    context_object_name = 'artwork'
    pk_url_kwarg = 'artwork_id'
