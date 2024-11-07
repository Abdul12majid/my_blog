from . import views
from django.urls import path, register_converter
import uuid

# Register a UUID path converter
class UUIDConverter:
    regex = '[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}'

    def to_python(self, value):
        return uuid.UUID(value)

    def to_url(self, value):
        return str(value)

register_converter(UUIDConverter, 'uuid')

urlpatterns = [
    path('', views.home, name="home"),
    path('check_username', views.check_username, name="check_username"),
    path('check_email', views.check_email, name="check_email"),
    path('check_password1', views.check_password1, name="check_password1"),
    path('check_password2', views.check_password2, name="check_password2"),
    path('like-count/<uuid:pk>/', views.like_count2, name='like_count2'),
    path('follow/<str:pk>/', views.follow, name='follow'),
    #path('unfollow/<str:pk>/', views.unfollow, name='unfollow'),
    
    
]
