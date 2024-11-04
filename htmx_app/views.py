from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User

# Create your views here.
def index(request):
	return HttpResponse("htmx")


def check_username(request):
	username = request.POST.get('username')
	if len(username) < 4:
		return HttpResponse("Username too short")
	if User.objects.filter(username=username).exists():
		return HttpResponse("Username taken")
	else:
		return HttpResponse("Username available")


def check_email(request):
	email = request.POST.get('email')
	if User.objects.filter(email=email).exists():
		return HttpResponse("email exists")
	else:
		return HttpResponse("email available")


def check_password1(request):
	password = request.POST.get('password1')
	if len(password) < 8:
		return HttpResponse("password too short")
	else:
		return HttpResponse("")


def check_password2(request):
	password = request.POST.get('password1')
	password2 = request.POST.get('password2')
	if password2 != password:
		return HttpResponse("password does not match")
	else:
		return HttpResponse("")