from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.contrib.auth.models import User
from blog_app.models import Post

# Create your views here.
def home(request):
	return HttpResponse("htmx")


def check_username(request):
	username = request.POST.get('username')
	if len(username) < 4:
		return HttpResponse("<p class='error'>Username too short</p>")
	if User.objects.filter(username=username).exists():
		return HttpResponse("<p class='error'>Username taken</p>")
	else:
		return HttpResponse("<p class='success'>Username available</p>")


def check_email(request):
	email = request.POST.get('email')
	if '@' not in email:
		return HttpResponse("<p class='error'>Invalid email</p>")
	if User.objects.filter(email=email).exists():
		return HttpResponse("<p class='error'>Email exixts</p>")
	else:
		return HttpResponse("<p class='success'>Email available</p>")


def check_password1(request):
	password = request.POST.get('password1')
	if len(password) < 8:
		return HttpResponse("<p class='error'>Password too short</p>")
	else:
		return HttpResponse("")


def check_password2(request):
	password = request.POST.get('password1')
	password2 = request.POST.get('password2')
	if password2 != password:
		return HttpResponse("<p class='error'>Password does not match</p>")
	else:
		return HttpResponse("")


def like_count2(request, pk):
    post = get_object_or_404(Post, id=pk)
    user_profile = request.user.profile
    
    if request.htmx:
        if post in user_profile.liked_post.all():
            user_profile.liked_post.remove(post)
            post.likes -= 1
            count = post.likes
            user_profile.save()
            post.save()	
            liked_post = user_profile.liked_post.all()
            context = {
            'post': post,
            'liked_post': liked_post,
            'count': count,
	        }
            return render(request, 'like_count.html', context)
        else:
        	user_profile.liked_post.add(post)
        	post.likes += 1
        	count = post.likes
        	user_profile.save()
        	post.save()
        	liked_post = user_profile.liked_post.all()
        	context = {
        	    'post': post,
	            'liked_post': liked_post,
	            'count': count,
	        }
        	return render(request, 'like_count.html', context)
    return HttpResponse("Invalid request")


def follow(request, pk):
	user = get_object_or_404(User, id=pk)
	get_user = request.user
	print(user.profile in get_user.profile.follows.all())
	if request.htmx:
		get_user.profile.follows.remove(user.profile)
		get_user.profile.save()
		context = {
			'user':user,
			'get_user':get_user,
		}
		return render(request, 'follow.html', context)
	return HttpResponse("Invalid request")


def unfollow(request, pk):
	user = get_object_or_404(User, id=pk)
	get_user = request.user
	print(user.profile in get_user.profile.follows.all())
	if request.htmx:
		get_user.profile.follows.add(user.profile)
		get_user.profile.save()
		context = {
			'user':user,
			'get_user':get_user,
		}
		return render(request, 'unfollow.html', context)
	return HttpResponse("Invalid request")