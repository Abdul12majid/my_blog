from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User

# Create your views here.
def index(request):
	return HttpResponse("htmx")


def check_username(request):
	username = request.POST.get('username')
	if User.objects.filter(username=username).exists():
		return HttpResponse("Username found")
	else:
		return HttpResponse("Username not found")