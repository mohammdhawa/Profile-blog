from django.urls import path
from . import views

app_name = 'base'

urlpatterns = [
    path('', views.home, name="home"),
    path('posts/', views.posts, name='posts'),
    path('post/', views.post, name="post"),
    path('profile/', views.profile, name='profile'),
]
