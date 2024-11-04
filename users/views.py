from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
	return render(request, "signin.html")


def signup(request):
	if request.POST:
		username = request.POST['username']
		email = request.POST['email']
		password1 = request.POST.get('password1')
		password2 = request.POST.get('password2')
		if password1 == password2:
			print('Password mismatch')	
		if User.objects.filter(username=username).exists():
			print('username exists')	
			
		user = User.objects.create_user(username=username, password=password2)
		user.save()
		get_user = authenticate(username=username, password=password2)
		login(request, get_user)
		return redirect('index')
	return render(request, 'register.html')