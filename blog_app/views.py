from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Post, Category
from django.contrib import messages

# Create your views here.

tech_category = Category.objects.get(id=1)
business_category = Category.objects.get(id=2)
random_category = Category.objects.get(id=3)
health_category = Category.objects.get(id=5)


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


def tech(request):
	tech_blog = Post.objects.filter(categories=tech_category).all().order_by('-created_at')
	most_liked_post = Post.objects.filter(categories=tech_category).all().order_by('-likes').first()
	context = {
		'tech_blog':tech_blog,
		'most_liked_post':most_liked_post
	}
	return render(request, 'pages/tech.html', context)

def business(request):
	business_blog = Post.objects.filter(categories=business_category).all().order_by('-created_at')
	most_liked_post = Post.objects.filter(categories=business_category).all().order_by('-likes').first()
	context = {
		'business_blog':business_blog,
		'most_liked_post':most_liked_post
	}
	return render(request, 'pages/business.html', context)


def random(request):
	random_blog = Post.objects.filter(categories=random_category).all().order_by('-created_at')
	most_liked_post = Post.objects.filter(categories=random_category).all().order_by('-likes').first()
	context = {
		'random_blog':random_blog,
		'most_liked_post':most_liked_post
	}
	return render(request, 'pages/random.html', context)


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    context = {
    	'post': post,
    }
    return render(request, 'pages/post_detail.html', context)