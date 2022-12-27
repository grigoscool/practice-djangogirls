from django.shortcuts import render
from django.utils import timezone

from .models import Post

def index(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by("-created_date")
    pub_post = []
    for post in posts:
        if post.published_date:
            pub_post.append(post)
    context = {'pub_post': pub_post}
    return render(request, 'blog/index.html', context)