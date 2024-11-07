from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from blog_app.models import Post


# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    contact = models.CharField(max_length=255)
    date_of_birth=models.DateTimeField(auto_now=True)
    profile_image = models.ImageField(upload_to='profile_images', null=True, blank=True)
    profile_bio=models.TextField(null=True, blank=True, max_length=500)
    liked_post = models.ManyToManyField(Post, symmetrical=False, blank=True)
    bookmarked = models.ManyToManyField(Post, related_name='saved_blog', symmetrical=False, blank=True)
    post_count = models.IntegerField(default=0)
    follows=models.ManyToManyField('self', related_name='followed_by', symmetrical=False, blank=True)

    def __str__(self):
        return self.user.username

def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile=Profile(user=instance)
        user_profile.save()
post_save.connect(create_profile, sender=User)