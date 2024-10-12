from django.shortcuts import render
from .models import BlogPost
from .serializers import BlogPostSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from UserAuth.models import User

# Create your views here.

# Blog Management
class BlogPostListCreateView(APIView):
    permission_classes=[IsAuthenticatedOrReadOnly]
    
    def get(self,request):
        user = request.user
        if user.is_admin or user.is_superuser:
           posts=BlogPost.objects.all()
           serializer=BlogPostSerializer(posts, many=True)
           return Response(serializer.data)
        else:
           posts=BlogPost.objects.filter(author=user)
           serializer=BlogPostSerializer(posts, many=True)
           return Response(serializer.data)
    
    def post(self,request):
        # author = User.objects.get(id = request.user.id)
        serializer=BlogPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class BlogPostRetrieveUpdateDeleteView(APIView):
    def get_object(self,post_id):
        return BlogPost.objects.get(pk=post_id)
    
    def get(self, request,post_id):
        post=self.get_object(post_id)
        serializer=BlogPostSerializer(post)
        return Response(serializer.data)
    
    def put(self,request,post_id):
        post=self.get_object(post_id)
        serializer=BlogPostSerializer(post,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,post_id):
        post=self.get_object(post_id)
        post.delete()
        return Response({'delete':'Delete SuccessFully'}, status=status.HTTP_204_NO_CONTENT)
     
