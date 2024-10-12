from django.urls import path
from .views import BlogPostListCreateView,BlogPostRetrieveUpdateDeleteView


urlpatterns = [
    path('post/',BlogPostListCreateView.as_view(),name='blogpost-list-create'),
    path('posts/<int:post_id>/',BlogPostRetrieveUpdateDeleteView.as_view(),name='blogpost-detail'),
]