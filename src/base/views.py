from django.shortcuts import render
# Create your views here.

def home(request):
    
    context = {}
    return render(request, 'base/index.html', context)

def posts(request):
    
    posts = [
        {
            'headline': 'Laboratory Management System',
            'sub_headline': 'Designed build & matained a the lab management system for FOI laboratory',
        },
        {
            'headline': 'Online Store - Course',
            'sub_headline': 'Online store with paypal payment integration and guest user shopping',
        },
        {
            'headline': 'Membership Website',
            'sub_headline': "Modulized guide for online courses with step by step instructions",
        }
    ]

    context = {'posts': posts}
    return render(request, 'base/posts.html', context)

def post(request):
    
    context = {}
    return render(request, 'base/post.html', context)

def profile(request):
    
    context = {}
    return render(request, 'base/profile.html', context)
