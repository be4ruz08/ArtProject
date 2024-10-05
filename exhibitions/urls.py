from django.urls import path
from . import views

urlpatterns = [
    path('', views.ExhibitionListView.as_view(), name='exhibition_list'),
    path('<int:exhibition_id>/', views.ExhibitionDetailView.as_view(), name='exhibition_detail'),
]
