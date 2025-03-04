from django.urls import path
from . import views

app_name = 'App_Blog'

urlpatterns = [
    path('', views.BlogList.as_view(), name='blog_list'),
    path('create_blog/', views.CreateBlog.as_view(), name='create_blog'),
    path('details/<slug>/', views.blog_detail, name='blog_detail'),
    path('liked/<pk>/', views.liked, name='liked'),
    path('unliked/<pk>/', views.disliked, name='unliked'),
    path('my_blogs/', views.MyBlogs.as_view(), name='myblogs'),
    path('edit_blog/<pk>/', views.UpdateBlog.as_view(), name='edit_blog'),


]
