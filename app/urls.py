from django.urls import path
from . import views

urlpatterns=[
    path('register/',views.RegistrationView.as_view(),name='RegistrationView'),#add a new user into db
    path('login/',views.UserLoginView.as_view(),name='UserLoginView'),#login
    # path('task/',views.TaskView.as_view(),name='TaskView'),
    path('tasks/', views.TaskList.as_view(), name='task-list'),
    path('tasks/<int:pk>/', views.TaskDetail.as_view(), name='task-detail'),
    path('tasks/<str:status>/', views.TaskListByStatus.as_view(), name='task-list-by-status'),
    # path('tasks/filter/', views.TaskFilterByStatus.as_view(), name='task-filter-by-status'),
    ]