from rest_framework import serializers
from .models import Comment
from UserAuth.serializers import UserRegistrationSerializer
from BlogAuth.serializers import BlogPostSerializer

class CommentSerializer(serializers.ModelSerializer):
    
    author = UserRegistrationSerializer(read_only=True)
    post = BlogPostSerializer(read_only=True)
    class Meta:
        model=Comment
        fields=['id','comment_content','publication_date','author','post']
        