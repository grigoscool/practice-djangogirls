from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('post_detail/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post_detail/<int:pk>/edit/', views.post_edit, name='post_edit'),
]
