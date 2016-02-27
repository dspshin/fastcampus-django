from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
	msg = 'hello world'
	return render( request, 'hello.html', {'message':msg} )