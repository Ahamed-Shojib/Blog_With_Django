from django.urls import path
from . import views

app_name = 'App_Blog'

urlpatterns = [
    path('', views.BlogList.as_view(), name='blog_list'),
    path('create_blog/', views.CreateBlog.as_view(), name='create_blog'),
    path('details/<slug>/', views.blog_detail, name='blog_detail'),
    #path(r'^blog_detail/(?P<slug>[-a-zA-Z0-9_.]+)/$', views.blog_detail, name='blog_detail'),


]
