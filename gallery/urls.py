from django.urls import path
from . import views

urlpatterns = [
    path('', views.artwork_list, name='artwork_list'),
    path('<int:artwork_id>/', views.artwork_detail, name='artwork_detail'),
]
