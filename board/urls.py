from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'board'
urlpatterns = [
	path('', views.index, name='index'),
	path('<int:post_id>/', views.postdetail, name='detail'),
]
