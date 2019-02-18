from django.db import models
# from django.core.files.storage import FileSystemStorage

# Create your models here.

class PageCounter(models.Model):
	total_count = models.IntegerField(default=0)

class Team(models.Model):
	full_name = models.CharField(max_length=100)
	position = models.CharField(max_length=100)
	image = models.ImageField(blank=True, null=True, upload_to="photos/%Y/%m/%D/")

	def __str__(self):
		return self.full_name

class Career(models.Model):
	title = models.CharField(max_length=100)
	pub_date = models.DateTimeField('date published')
	due_date = models.DateTimeField('due date')
	job_des = models.CharField(max_length=500)
	qualification = models.CharField(max_length=200)

	def __str__(self):
		return self.title