from django.contrib import admin
from django.urls import path, include
from . import views	

app_name = 'members'
urlpatterns = [
	path('', views.index, name='index'),
	path('jobrequest/', views.jobrequest, name='jobrequest'),
	path('<int:job_id>/', views.detail, name='detail'),
]