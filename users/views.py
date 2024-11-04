from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
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

		if password1 != password2:
			print('Password mismatch')	
		if User.objects.filter(username=username).exists():
			print('username exists')	
			
		user = User.objects.create_user(username=username, password=password2)
		user.save()
		get_user = authenticate(username=username, password=password2)
		login(request, get_user)
		return redirect('index')

	return render(request, 'register.html')