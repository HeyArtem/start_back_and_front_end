from blog_app.api.serializers import BlogPostListSerializer
from rest_framework import generics
from blog_app.models import BlogPost


class BlogPostListAPIView(generics.ListAPIView):
    queryset = BlogPost.objects.filter(status='published')
    serializer_class = BlogPostListSerializer
