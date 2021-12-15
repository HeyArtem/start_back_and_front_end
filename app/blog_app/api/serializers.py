from blog_app.models import BlogPost, BlogCategory, BlogTag
from rest_framework import fields, serializers


class BlogPostCategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = BlogCategory
        fields = '__all__'
        
        
class BlogPostTagSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = BlogCategory
        fields = '__all__'
        

class BlogPostListSerializer(serializers.ModelSerializer):
    category = BlogPostCategorySerializer()
    tag = BlogPostTagSerializer(many=True)
    
    class Meta:
        model = BlogPost
        fields = [
            'id',
            'title',
            'img',
            'category',
            'description',
            'tag',
            'updated_at'
        ]
