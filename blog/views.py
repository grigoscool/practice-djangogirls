from django.shortcuts import render, get_object_or_404,redirect
from django.utils import timezone
from .form import PostForm

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

def post_new(request):

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
        return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_new.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
        return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_new.html', {'form': form})