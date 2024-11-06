from . import views
from django.urls import path

urlpatterns = [
    path('signin', views.signin, name="signin"),
    path('signup', views.signup, name="signup"),
    path('logout', views.logout_user, name="logout"),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('my_blogs', views.my_blogs, name="my_blogs"),
    path('saved_blogs', views.saved_blogs, name="saved_blogs"),
    path('following', views.following, name="following"),
    path('followers', views.followers, name="followers"),

    
    
]
