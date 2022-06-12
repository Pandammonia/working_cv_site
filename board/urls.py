from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'board'
urlpatterns = [
	path('', views.index, name='index'),
	path('<slug:slug>/', views.postdetail, name='detail'),
	path('newmsg/', views.newmsg, name='newmsg'),
	path('newreply/<int:post_id>/', views.newreply, name='newreply'),
]
