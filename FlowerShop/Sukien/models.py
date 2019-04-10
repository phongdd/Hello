from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
	def __str__(self):
		return self.title
		
	title = models.CharField(max_length = 255, blank = False, null = False)
	content = models.TextField(max_length = 1000, blank = False, null = False)
	time_create = models.DateTimeField(default = timezone.datetime.now())
		