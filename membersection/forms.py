from django import forms
from .models import JobRequest, JobRequestReply

class JobRequestForm(forms.ModelForm):
	class Meta:
		model = JobRequest
		fields = ['jobtitle', 'jobdesc', 'price']

class JobRequestReplyForm(forms.ModelForm):
	class Meta:
		model = JobRequestReply 
		fields = ['subject', 'reply']