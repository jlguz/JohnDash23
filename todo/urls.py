from django.urls import path
from . views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete, CustomLoginView, RegisterPage

from django.contrib.auth.views import LogoutView

urlpatterns = [

    path('todo_login/', CustomLoginView.as_view(), name='todo_login'),
    path('todo_logout/', LogoutView.as_view(next_page='todo_login'), name='todo_logout'),
    path('todo_register/', RegisterPage.as_view(), name='todo_register'),
    

    path('task_list/', TaskList.as_view(), name='task_list'),
    path('task_detail/<int:pk>/', TaskDetail.as_view(), name='task_detail'),
    path('create_task/', TaskCreate.as_view(), name='create_task'),
    path('update_task/<int:pk>/', TaskUpdate.as_view(), name='update_task'),
    path('delete_task/<int:pk>/', TaskDelete.as_view(), name='delete_task'),
]