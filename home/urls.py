from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.home, name='index'),
    path('lottery/', views.lottery, name='lottery'),
    path('/lottery1', views.lottery1, name='lottery1')
]

