from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import PostEditForm

from django.core.paginator import Paginator
from django.core.paginator import PageNotAnInteger, EmptyPage

from django.contrib.auth.decorators import login_required

def list(request):
	per_page = 5
	cur_page = request.GET.get('page',1)
	posts = Post.objects.select_related().order_by('-created_at')
	paginator = Paginator(posts, per_page)
	try:
		page = paginator.page(cur_page)
	except PageNotAnInteger:
		page = paginator.page(1)
	except EmptyPage:
		page = []
	return render( request, 'list.html', {
		'posts':page
	})

def post(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'post.html', {
		'post':post
	})

from .models import Category
from django.shortcuts import redirect

@login_required
def create(request):
	#if not request.user.is_authenticated():
	#	raise Exception('who are you???')

	if request.method == 'GET':
		form = PostEditForm()
	elif request.method == 'POST':
		form = PostEditForm(request.POST)
		if form.is_valid():
			new_post = form.save()
			return redirect('view_post', pk=new_post.pk)

	categories = Category.objects.all()
	return render(request, 'create.html', {
		'categories':categories,
		'form':form
	})