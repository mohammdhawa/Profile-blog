from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required   
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
# Create your views here.

from .models import Tag, Post
from .forms import PostForm
from .filters import PostFilter

def home(request):
    posts = Post.objects.filter(active=True, featured=True)[:3]

    context = {'posts': posts}
    return render(request, 'base/index.html', context)

def posts(request):
    posts = Post.objects.filter(active=True)
    myFilter = PostFilter(request.GET, queryset=posts)
    posts = myFilter.qs

    page = request.GET.get('page')

    paginator = Paginator(posts, 3)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {'posts': posts, 'myFilter': myFilter}
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


def sendEmail(request):

    if request.method == 'POST':
        template = render_to_string('base/email_template.html', {
            'name': request.POST['name'],
            'email': request.POST['email'],
            'message': request.POST['message'],
        })

        email = EmailMessage(
            request.POST['subject'],
            template,
            settings.EMAIL_HOST_USER,
            ['ismekbektop@gmail.com']
        )
        email.fail_silently = False
        email.send()

    context = {}
    return render(request, 'base/email_sent.html', context)