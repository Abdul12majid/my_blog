from django.shortcuts import render, HttpResponse
from .models import Post, Category

# Create your views here.

world_category = Category.objects.get(id=3)
health_category = Category.objects.get(id=5)
tech_category = Category.objects.get(id=1)

def index(request):
	the_blog = Post.objects.order_by('-likes').first()
	get_tech_blog = Post.objects.filter(categories=tech_category).all()
	most_liked_tech = get_tech_blog.order_by('-likes').first()



	context = {
	'the_blog':the_blog,
	'most_liked_tech':most_liked_tech,
	}
	return render(request, 'index.html', context)