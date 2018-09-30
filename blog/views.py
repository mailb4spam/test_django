from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def post_list(request):
	return render(request, 'blog/post_list.html',{})

def index(request):
    return HttpResponse('Hello, welcome to the index page.')

def individual_post(request):
    return HttpResponse('Hi, this is where an individual post will be.')

