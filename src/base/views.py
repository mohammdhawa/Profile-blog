from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required   
# Create your views here.

from .models import Tag, Post
from .forms import PostForm

def home(request):
    posts = Post.objects.filter(active=True, featured=True)[:3]

    context = {'posts': posts}
    return render(request, 'base/index.html', context)

def posts(request):
    posts = Post.objects.filter(active=True)

    context = {'posts': posts}
    return render(request, 'base/posts.html', context)

def post(request, pk):
    post = Post.objects.get(id=pk)

    context = {'post': post}
    return render(request, 'base/post.html', context)

def profile(request):
    
    context = {}
    return render(request, 'base/profile.html', context)


# CRUD views

@login_required(login_url="base:home")
def createPost(request):
    form = PostForm()

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('base:posts')

    context = {'form': form}
    return render(request, 'base/post_form.html', context)


@login_required(login_url="base:home")
def updatetPost(request, pk):
    post = Post.objects.get(id=pk)

    form = PostForm(instance=post)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
        return redirect('base:posts')

    context = {'form': form}
    return render(request, 'base/post_form.html', context)


@login_required(login_url="base:home")
def deletePost(request, pk):
    post = Post.objects.get(id=pk)

    if request.method == 'POST':
        post.delete()
        return redirect("base:posts")

    context = {'item': post}
    return render(request, 'base/delete.html', context)