from . import views
from django.urls import path

urlpatterns = [
    path('signin', views.signin, name="signin"),
    path('signup', views.signup, name="signup"),
    path('logout', views.logout_user, name="logout"),
    path('profile', views.profile, name="profile"),
    
    
]
