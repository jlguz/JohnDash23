from django.urls import path
from . import views

urlpatterns = [

    path('crm_home/', views.home, name='crm_home'),
    

    # CRUD


]
