from django.shortcuts import render
# Create your views here.

def home(request):
    
    context = {}
    return render(request, 'base/home.html', context)

def posts(request):

    context = {}
    return render(request, 'base/posts.html', context)

def post(request):
    
    context = {}
    return render(request, 'base/post.html', context)

def profile(request):
    
    context = {}
    return render(request, 'base/profile.html', context)
