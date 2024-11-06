from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import Post, Category
from django.contrib import messages

# Create your views here.

tech_category = Category.objects.get(id=1)
business_category = Category.objects.get(id=2)
random_category = Category.objects.get(id=3)
health_category = Category.objects.get(id=5)


def index(request):
	most_liked_post = Post.objects.order_by('-likes').first()
	user_profile = request.user.profile
	liked_post = user_profile.liked_post.all()

	# Get the second and third most liked posts
	top_three_posts = Post.objects.order_by('-likes')[:3]

	second_most_liked_post = top_three_posts[1] if len(top_three_posts) > 1 else None
	third_most_liked_post = top_three_posts[2] if len(top_three_posts) > 2 else None

	context = {
		'most_liked_post':most_liked_post,
		'second_most_liked_post':second_most_liked_post,
		'third_most_liked_post':third_most_liked_post,
		'liked_post':liked_post,
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
    user_profile = request.user.profile
    liked_post = user_profile.liked_post.all()
    context = {
    	'post': post,
    	'user_profile': user_profile,
    	"liked_post": liked_post,
    }
    return render(request, 'pages/post_detail.html', context)


def like_blog(request, pk):
	post = get_object_or_404(Post, id=pk)
	user_profile = request.user.profile
	if post in user_profile.liked_post.all():
		user_profile.liked_post.remove(post)
		user_profile.save()
		post.likes -= 1
		post.save()
		return redirect(request.META.get("HTTP_REFERER"))
	else:
		user_profile.liked_post.add(post)
		user_profile.save()
		post.likes += 1
		post.save()
		return redirect(request.META.get("HTTP_REFERER"))
	return redirect(request.META.get("HTTP_REFERER"))