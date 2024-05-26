"""
URL configuration for merchex project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from taskman import views





urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),

    path('accounts/', include('accounts.urls')),


    path('task/', views.task, name = 'task'),

    


    path('task/update/<int:task_id>/', views.update_task, name='update_task'),
    
    path('task/updatee/<int:task_id>/', views.update_taskk, name='update_taskk'),


    path('task/edit/<int:task_id>/', views.edit_task, name='edit_task'),


    path('task/editt/<int:task_id>/', views.edit_taskk, name='edit_taskk'),


    path('task/delete/<int:task_id>/', views.delete_task, name='delete_task'),

    path('task/detail/<int:task_id>/', views.detail_task, name='detail_task'),

    path('task/create/', views.create_task, name='create_task'),


    path('chat/', views.chat, name='chat'),

    path('chat/update/<int:chat_id>/', views.update_chat, name='update_chat'),

    path('chat/edit/<int:chat_id>/', views.edit_chat, name='edit_chat'),

    path('chat/delete/<int:chat_id>/', views.delete_chat, name='delete_chat'),

    path('chat/detail/<int:chat_id>/', views.detail_chat, name='detail_chat'),

    path('chat/create/', views.create_chat, name='create_chat'),


                          







]
