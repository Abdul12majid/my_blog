from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name="index"),
    path('health', views.health, name="health"),
    path('technology', views.tech, name="technology"),
    path('business', views.business, name="business"),
    path('random', views.random, name="random"),
    
]
