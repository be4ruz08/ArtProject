from django.shortcuts import render, get_object_or_404
from .models import BlogPost


def post_list(request):
    posts = BlogPost.objects.all().order_by('-published_at')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    return render(request, 'blog/post_detail.html', {'post': post})
