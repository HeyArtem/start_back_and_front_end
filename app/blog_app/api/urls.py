from django.urls import path
from blog_app.api.views import BlogPostListAPIView

urlpatterns = [
    path('', BlogPostListAPIView.as_view())
]
