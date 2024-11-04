from django.shortcuts import render, HttpResponse
from .models import Post, Category

# Create your views here.

health_category = Category.objects.get(id=5)
tech_category = Category.objects.get(id=1)

def index(request):
	most_liked_post = Post.objects.order_by('-likes').first()

	# Get the second and third most liked posts
	top_three_posts = Post.objects.order_by('-likes')[:3]

	second_most_liked_post = top_three_posts[1] if len(top_three_posts) > 1 else None
	third_most_liked_post = top_three_posts[2] if len(top_three_posts) > 2 else None

	context = {
	'most_liked_post':most_liked_post,
	'second_most_liked_post':second_most_liked_post,
	'third_most_liked_post':third_most_liked_post
	}
	return render(request, 'index.html', context)



def health(request):
	health_blog = Post.objects.filter(categories=health_category).all().order_by('-created_at')
	most_liked_post = Post.objects.filter(categories=health_category).all().order_by('-likes').first()
	context = {
		'health_blog':health_blog,
		'most_liked_post':most_liked_post
	}
	return render(request, 'pages/health.html', context)