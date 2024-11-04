from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User

# Create your views here.
def index(request):
	return HttpResponse("htmx")


def check_username(request):
	username = request.POST.get('username')
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