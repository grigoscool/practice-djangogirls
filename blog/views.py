from django.shortcuts import render
from django.utils import timezone

from .models import Post

def index(request):
    pub_posts = Post.objects.filter(published_date__lte=timezone.now()).order_by("-created_date")
    posts = []
    for post in pub_posts:
        if post.published_date:
            posts.append(post)
    context = {'posts': posts}
    return render(request, 'blog/index.html', context)