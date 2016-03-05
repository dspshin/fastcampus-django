from django import forms
from .models import Post
from django.forms import ValidationError

class PostForm(forms.Form):
	title = forms.CharField()
	content = forms.CharField(widget=forms.Textarea)

class PostEditForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'content', 'tags', )
		#fields = '__all__'
	def clean_title(self):
		title = self.cleaned_data.get('title', '')
		if '바보' in title:
			raise ValidationError('invalid word')
		return title.strip()
	def clean(self):
		# 마지막으로 전체적인 validation을 체크하도록 한다.
		super(PostEditForm, self).clean()
		title = self.cleaned_data.get('title', '')
		content = self.cleaned_data.get('content', '')

		if 'asd' in title:
			self.add_error('title', 'asd cannot be included in title')