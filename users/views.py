from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from blog_app.models import Post

# Create your views here.

def signin(request):

	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = User.objects.filter(username=username).exists()
		if user is True:
			get_user = User.objects.get(username=username)
			user_username = get_user.username
			auth_user = authenticate(request, username=user_username, password=password)
			if auth_user is not None:
				login(request, get_user)
				print('login Successful')
				messages.success(request, 'Login Successful')
				return redirect('index')

			messages.success(request, 'Invalid username or password')
			return render(request, 'signin.html')
		return redirect('signup')
	return render(request, 'signin.html')


def signup(request):
	if request.POST:

		username = request.POST['username']
		email = request.POST['email']
		password1 = request.POST.get('password1')
		password2 = request.POST.get('password2')

		if User.objects.filter(username=username).exists():
			print('username exists')
			messages.success(request, 'Username exists, pick another.')
			return redirect('signup')
		if User.objects.filter(email=email).exists():
			print('email exists')
			messages.success(request, 'Email exists, pick another.')
			return redirect('signup')
		if password1 != password2:
			print('Password mismatch')
			messages.success(request, "Password doesn't match.")
			return redirect('signup')
			
		user = User.objects.create_user(username=username, password=password2, email=email)
		user.save()
		get_user = authenticate(username=username, password=password2)
		login(request, get_user)
		get_user = request.user
		messages.success(request, f"Welcome {get_user.username}, registration Successful.")
		return redirect('index')

	return render(request, 'signup.html')


def logout_user(request):
	logout(request)
	messages.success(request, "You've been logged out")
	return redirect('index')


def profile(request, username):
	user = get_object_or_404(User, username=username)
	get_user = request.user
	get_user_profile = get_user.profile.follows.all()
	context = {
		'user':user,
		'get_user':get_user,
		'get_user_profile':get_user_profile,
	}
	return render(request, 'profile.html', context)


def my_blogs(request, username):
	user = User.objects.get(username=username)
	user_profile = user.profile
	posts = Post.objects.filter(author=user).all
	context = {
		'posts':posts,
		'user':user,
	}
	return render(request, 'my_blogs.html', context)


def saved_blogs(request, username):
	user = User.objects.get(username=username)
	user_profile = user.profile
	posts = user_profile.bookmarked.all()
	context = {
		'posts':posts,
		'user':user,
	}
	return render(request, 'saved_blogs.html', context)


def following(request, username):
	user = User.objects.get(username=username)
	user_profile = user.profile
	follows = user_profile.follows.all()
	context = {
		'follows':follows,
		'user':user,
	}
	return render(request, 'following.html', context)


def followers(request, username):
	user = User.objects.get(username=username)
	user_profile = user.profile
	followers = user_profile.followed_by.all()
	context = {
		'followers':followers,
		'user':user,
	}
	return render(request, 'followers.html', context)

def test_base(request):
	return render(request, 'test_base.html')



def change_details(request):
	if request.method == "POST":
		user = request.user
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		email = request.POST['email']
		username = request.POST['username']
		user.first_name = first_name
		user.last_name = last_name
		user.email = email
		user.username = username
		user.save()
		print("changes made")
		messages.success(request, ("Info Updated."))
		return redirect(f"profile/{user.username}")
	return HttpResponse("invalid request")
