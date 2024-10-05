from django.views.generic import ListView, DetailView
from .models import Artist
from gallery.models import ArtWork


class ArtistListView(ListView):
    model = Artist
    template_name = 'artists/artist_list.html'
    context_object_name = 'artists'


class ArtistDetailView(DetailView):
    model = Artist
    template_name = 'artists/artist_detail.html'
    context_object_name = 'artist'
    pk_url_kwarg = 'artist_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['artworks'] = ArtWork.objects.filter(artist=self.object)
        return context
