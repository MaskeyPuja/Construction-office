from django.db import models
# from django.core.files.storage import FileSystemStorage

# Create your models here.

class PageCounter(models.Model):
	total_count = models.IntegerField(default=0)

class Team(models.Model):
	full_name = models.CharField(max_length=100)
	position = models.CharField(max_length=100)
	# image = models.FileField(storage=FileSystemStorage(location=MEDIA_ROOT), upload_to='photos/%Y/%m/%d')

	image = models.ImageField(blank=True, null=True, upload_to="photos/%Y/%m/%D/")
