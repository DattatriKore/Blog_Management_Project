from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
#Blog Management
class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    author_profile_picture=models.ImageField(upload_to='profile_picture/',blank=True,null=True)
    
    def __str__(self):
        return self.title