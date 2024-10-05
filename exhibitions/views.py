from django.views.generic import ListView, DetailView
from .models import Exhibition


class ExhibitionListView(ListView):
    model = Exhibition
    template_name = 'exhibitions/exhibition_list.html'
    context_object_name = 'exhibitions'


class ExhibitionDetailView(DetailView):
    model = Exhibition
    template_name = 'exhibitions/exhibition_detail.html'
    context_object_name = 'exhibition'
    pk_url_kwarg = 'exhibition_id'
