from django.db import models

# Create your models here.
class Post(models.Model):
	username = models.CharField(max_length=40)
	content = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return '{}번 글'.format(self.pk)