from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

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
