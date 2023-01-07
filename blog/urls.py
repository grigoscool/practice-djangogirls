from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('post_detail/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post_detail/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('draft/', views.show_draft_list, name='draft'),
    path('post/<pk>/publish/', views.post_publish, name='post_pub'),
    path('post/<pk>/remove/', views.post_remove, name='post_remove'),
    path('post/<pk>/comment', views.add_comment_to_post, name='add_comment'),
]
