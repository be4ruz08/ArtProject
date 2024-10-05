from django.urls import path
from . import views

urlpatterns = [
    path('', views.ArtistListView.as_view(), name='artist_list'),
    path('<int:artist_id>/', views.ArtistDetailView.as_view(), name='artist_detail'),
]
