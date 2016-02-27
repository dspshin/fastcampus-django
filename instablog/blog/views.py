from django.shortcuts import render, get_object_or_404
from .models import Post

from django.core.paginator import Paginator
from django.core.paginator import PageNotAnInteger, EmptyPage
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
def create(request):
	if request.method == 'GET':
		pass
	elif request.method == 'POST':
		new_post = Post()
		new_post.title = request.POST.get('title')
		new_post.content = request.POST.get('content')
		category_pk = request.POST.get('category')
		try:
			new_post.category = Category.objects.get(pk=category_pk)
		except: #category가 없는 경우에 대한 예외처리 해야함.
			pass
		new_post.save()
		return redirect('view_post', pk=new_post.pk)

	categories = Category.objects.all()
	return render(request, 'create.html', {
		'categories':categories
	})