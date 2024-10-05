from django.urls import path
from . import views

urlpatterns = [
    path('', views.ArtWorkListView.as_view(), name='artwork_list'),
    path('<int:artwork_id>/', views.ArtWorkDetailView.as_view(), name='artwork_detail'),
]
