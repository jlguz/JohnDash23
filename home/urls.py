from django.urls import path
from . import views

urlpatterns = [
    
    path('index', views.home, name='index'),
    path('register', views.register, name='register'),
    path('', views.my_login, name=''),
    path('user-logout', views.user_logout, name='user-logout'),
]

