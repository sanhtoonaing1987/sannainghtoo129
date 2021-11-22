from django.db import models

class Record(models.Model):
	title = models.CharField(max_length=255)
	content = models.TextField()
	date = models.DateField()
	
	def __str__(self):
		return self.title

# Create your models here.
