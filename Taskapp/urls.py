from django.urls import path
from . import views
from .views import TaskList, TaskDetailView, TaskCreateView, \
                    TaskUpdateView, TaskDeleteView, TaskLoginView, TaskRegisterView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', TaskList.as_view(), name='tasks'),
    path('login/', TaskLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', TaskRegisterView.as_view(), name='register'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name='task'),
    path('create-task/', TaskCreateView.as_view(), name='task-create'),
    path('update-task/<int:pk>/', TaskUpdateView.as_view(), name='task-update'),
    path('delete-task/<int:pk>/', TaskDeleteView.as_view(), name='task-delete'),
]












