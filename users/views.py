from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User

# Create your views here.

def signin(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password1']
		user = User.objects.filter(username=username).exists()
		if user is True:
			get_user = User.objects.get(username=username)
			user_username = get_user.username
			auth_user = authenticate(request, username=user_username, password=password)
			if auth_user is not None:
				login(request, get_user)
				return redirect('index')
			return render(request, 'login.html')
		return redirect('register')
	return render(request, 'login.html')


def signup(request):
	if request.POST:

		username = request.POST['username']
		email = request.POST['email']
		password1 = request.POST.get('password1')
		password2 = request.POST.get('password2')

		if User.objects.filter(username=username).exists():
			print('username exists')
		if User.objects.filter(email=email).exists():
			print('email exists')
		if password1 != password2:
			print('Password mismatch')
			
		user = User.objects.create_user(username=username, password=password2, email=email)
		user.save()
		get_user = authenticate(username=username, password=password2)
		login(request, get_user)
		return redirect('signup')

	return render(request, 'signup.html')