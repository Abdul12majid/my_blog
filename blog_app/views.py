from django.shortcuts import render, HttpResponse
from .models import Post

# Create your views here.

def index(request):
	the_blog = Post.objects.order_by('-likes').first()
	context = {
	'the_blog':the_blog,
	}
	return render(request, 'index.html', context)