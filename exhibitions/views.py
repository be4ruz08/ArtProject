from django.shortcuts import render, get_object_or_404
from .models import Exhibition


def exhibition_list(request):
    exhibitions = Exhibition.objects.all()
    return render(request, 'exhibitions/exhibition_list.html', {'exhibitions': exhibitions})


def exhibition_detail(request, exhibition_id):
    exhibition = get_object_or_404(Exhibition, id=exhibition_id)
    return render(request, 'exhibitions/exhibition_detail.html', {'exhibition': exhibition})
