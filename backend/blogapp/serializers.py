from rest_framework import serializers
from .models import Blog

class BlogSerializers(serializers.ModelSerializer):
    class Meta:
        model=Blog
       
        fields=("id","blog_title", "blog_post","author","date_published","blog_image")