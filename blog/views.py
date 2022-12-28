from django.shortcuts import render, get_object_or_404
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

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post.html', {'post': post})