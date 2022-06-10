from django.urls import path
from . import views
from cv import settings
from django.conf.urls.static import static 
app_name = 'pages'
urlpatterns = [
	path('', views.homepage, name='home'),
	path('projects/', views.projects, name='projects'),
	path('projects/<int:projid>/', views.projectdetail, name='projectdetail'),
	path('about/', views.about, name='about'),	
]

