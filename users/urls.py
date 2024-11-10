from . import views
from django.urls import path

urlpatterns = [
    path('signin', views.signin, name="signin"),
    path('signup', views.signup, name="signup"),
    path('logout', views.logout_user, name="logout"),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('my_blogs/<str:username>/', views.my_blogs, name="my_blogs"),
    path('saved_blogs/<str:username>/', views.saved_blogs, name="saved_blogs"),
    path('following/<str:username>/', views.following, name="following"),
    path('followers/<str:username>/', views.followers, name="followers"),
    path('change_details', views.change_details, name="change_details"),
    path('test_base', views.test_base, name="test_base"),

    
    
]
