from django.urls import path
from . import views

urlpatterns = [
    path('', views.exhibition_list, name='exhibition_list'),
    path('<int:exhibition_id>/', views.exhibition_detail, name='exhibition_detail'),
]
