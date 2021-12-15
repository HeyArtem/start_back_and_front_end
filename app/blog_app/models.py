from django.db import models


class BlogCategory(models.Model):
    title = models.CharField(max_length=30)
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        
    def __str__(self) -> str:
        return self.title


class BlogTag(models.Model):
    title = models.CharField(max_length=30)
    
    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"
        
    def __str__(self) -> str:
        return self.title


class BlogPost(models.Model):
    STATUS_CHOICES = (
        ("draft", "Draft"),
        ("published", "Published")
    )
    title = models.CharField(max_length=300)
    img = models.ImageField(upload_to="blog_app/")
    category = models.ForeignKey(BlogCategory, on_delete=models.SET_NULL, null=True)
    description = models.CharField(max_length=200)
    content = models.TextField()
    tag = models.ManyToManyField(BlogTag, blank=True)    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS_CHOICES, default='draft', max_length=15)
    
    class Meta:
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"
        
    def __str__(self) -> str:
        return self.title
