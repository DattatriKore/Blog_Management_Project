
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings

# Create your models here.
class Comment(models.Model):
    comment_content=models.TextField()
    publication_date=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    post=models.ForeignKey('BlogAuth.BlogPost',on_delete=models.CASCADE,related_name='comments')


