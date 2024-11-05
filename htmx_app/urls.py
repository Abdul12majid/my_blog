from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name="home"),
    path('check_username', views.check_username, name="check_username"),
    path('check_email', views.check_email, name="check_email"),
    path('check_password1', views.check_password1, name="check_password1"),
    path('check_password2', views.check_password2, name="check_password2"),
    
    
]
