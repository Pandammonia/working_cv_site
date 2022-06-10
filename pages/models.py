from django.db import models

class Project(models.Model):
	title = models.CharField(max_length=140)
	desc = models.TextField()
	date = models.DateTimeField(auto_now_add=True)
	projectimage = models.FileField(blank=True, null=True)


	