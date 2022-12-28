from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('post_detail/<int:pk>/', views.post_detail, name='post_detail'),
]
