from django.shortcuts import render
from .models import Project


def homepage(request):
	return render(request, 'pages/home.html')

def projects(request):
	projects = Project.objects.order_by('date')
	context = {'projects':projects}
	return render(request, 'pages/projects.html', context)

def projectdetail(request, projid):
	project = Project.objects.get(id=projid)
	context = {'project':project}
	return render(request, 'pages/projectdetail.html', context)

def about(request):
	return render(request, 'pages/about.html')

