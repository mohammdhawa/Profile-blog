from django.urls import path
from . import views

app_name = 'base'

urlpatterns = [
    path('', views.home, name="home"),
    path('posts/', views.posts, name='posts'),
    path('post/<slug:pk>/', views.post, name="post"),
    path('profile/', views.profile, name='profile'),

    # CRUD Paths

    path('create_post/', views.createPost, name='create_post'),
    path('update_post/<slug:pk>/', views.updatetPost, name='update_post'),
    path('delete_post/<slug:pk>/', views.deletePost, name="delete_post"),

    path("send_email/", views.sendEmail, name="send_email"),
]
