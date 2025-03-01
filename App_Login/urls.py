from django.urls import path
from App_Login import views

app_name = 'App_Login'

urlpatterns = [
    path('signup/', views.signUp, name='signup'),
    path('login/', views.LogIn, name='login'),
    path('logout/', views.LogOut, name='logout'),
    path('logout_x/', views.LogOut_X, name='logout_x'),
    path('userhome/', views.user_home, name='user_home'),
    path('userprofile/', views.user_profile, name='user_profile'),
    path('changeprofile/', views.change_profile, name='change_profile'),
    path('password/', views.change_password, name='change_password'),
    path('addpropic/', views.add_profile_pic, name='add_profile_pic'),
    path('change-pro-pic',views.change_profile_pic, name='change_profile_pic'),
]

