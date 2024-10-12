from rest_framework import serializers
from .models import BlogPost

# Blog Management
class BlogPostSerializer(serializers.ModelSerializer):
    author_profile_picture=serializers.ImageField(required=False)
    class Meta:
        model=BlogPost
        fields=['id','title','content','publication_date','author','author_profile_picture']
    
    def create(self,validated_data):
        author_profile_picture=validated_data.pop('author_profie_picture',None)
        blog_post=BlogPost.objects.create(**validated_data)
        if author_profile_picture:
            blog_post.author_profile_picture=author_profile_picture
            blog_post.save()
        return blog_post
    
    def update(self,instance,validated_data):
        author_profile_picture=validated_data.pop('author_profile_picture',None)
        instance=super().update(instance,validated_data)
        if author_profile_picture is not None:
            if author_profile_picture:
                instance.author_profile_picture=author_profile_picture
            else:
                instance.author_profile_picture.delete()
            instance.save()
        return instance