from django.contrib import admin
from django.urls import path,include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('App_Blog.urls')),
    path('account/', include('App_Login.urls')),
    path('', views.home, name='home'),
]
