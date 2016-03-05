from django.db import models
from django.conf import settings

class Post(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	title = models.CharField(max_length=200)
	content = models.TextField()
	tags = models.ManyToManyField('Tag') #문자열로 모델명을 넣어줘도 됨.
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	is_model_field = False
	class Meta:
		ordering=('-updated_at', '-pk')
	def __str__(self):
		return '{}:{}'.format(self.pk, self.title)

class Category(models.Model):
	post = models.ForeignKey(Post)
	name = models.CharField(max_length=40, null=True)
	def __str__(self):
		return '{}:{}'.format(self.pk, self.name)

class Comment(models.Model):
	post = models.ForeignKey(Post)
	content = models.TextField(max_length=500)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	def __str__(self):
		return '{}:{}'.format(self.pk, self.post)

class Tag(models.Model):
	name = models.CharField(max_length=40)
	def __str__(self):
		return '{}:{}'.format(self.pk, self.name)
