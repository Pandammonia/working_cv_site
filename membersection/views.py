from django.shortcuts import render,redirect
from .models import JobRequest, JobRequestReply
from django.contrib.auth.decorators import login_required
from .forms import JobRequestForm
from django.http import Http404
@login_required
def index(request):
	requests = JobRequest.objects.order_by('added')
	context = {'requests':requests}
	return render(request, 'membersection/index.html', context)

def jobrequest(request):
	if request.method == 'POST':
		form = JobRequestForm(data=request.POST)
		if form.is_valid():
			new_form = form.save(commit=False)
			new_form.owner = request.user
			new_form.save()
			return redirect('members:index')
	else:
		form = JobRequestForm()
	context = {'form': form}
	return render(request, 'membersection/jobrequest.html', context)

def detail(request, job_id):
	job = JobRequest.objects.get(id=job_id)
	if job.owner != request.user:
		raise Http404
	context = {'job':job}
	return render(request, 'membersection/detail.html', context)


