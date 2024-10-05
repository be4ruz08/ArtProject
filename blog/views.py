from django.views.generic import ListView, DetailView
from .models import BlogPost


class PostListView(ListView):
    model = BlogPost
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    ordering = ['-published_at']


class PostDetailView(DetailView):
    model = BlogPost
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'
    pk_url_kwarg = 'post_id'
