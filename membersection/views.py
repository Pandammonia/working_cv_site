from django.shortcuts import render
from .models import JobRequest, JobRequestReply
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
	return render(request, 'membersection/index.html',)

