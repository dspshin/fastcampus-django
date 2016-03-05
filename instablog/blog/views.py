from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import PostForm

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
		form = PostForm()
	elif request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
		  	new_post = Post()
		  	new_post.title = form.cleaned_data.get('title')
		  	new_post.content = form.cleaned_data['content']
		  	category_pk = request.POST.get('category')
		  	category = get_object_or_404(Category, pk=category_pk)
		  	new_post.category = category
		  	new_post.save()
		  	return redirect('view_post', pk=new_post.pk)

	categories = Category.objects.all()
	return render(request, 'create.html', {
		'categories':categories,
		'form':form
	})