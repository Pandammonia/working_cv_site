from django.contrib import admin
from .models import JobRequest, JobRequestReply

admin.site.register(JobRequest)
admin.site.register(JobRequestReply)
# Register your models here.
