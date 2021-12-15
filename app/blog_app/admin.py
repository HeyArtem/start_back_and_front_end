from django.contrib import admin
from .models import BlogPost, BlogCategory, BlogTag

admin.site.register(BlogPost),
admin.site.register(BlogCategory),
admin.site.register(BlogTag)
