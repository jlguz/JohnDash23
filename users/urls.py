from django.urls import path
from .  import views

urlpatterns = [

    path('register/', views.register,name='register'),
    path('', views.loginpage, name='login'),
    path('logout/', views.logoutuser, name='logout'),

]