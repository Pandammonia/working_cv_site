from django.db import models
from django.conf import settings

class JobRequest(models.Model):
	owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	jobtitle = models.CharField(max_length=180)
	jobdesc = models.TextField()
	added = models.DateTimeField(auto_now_add=True)
	price = models.DecimalField(decimal_places=2, max_digits=10)

	def __str__(self):
		return self.jobtitle

class JobRequestReply(models.Model):
	owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	subject = models.CharField(max_length=80)
	reply = models.TextField()
	added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.subject