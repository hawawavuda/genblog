from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import BlogSerializers
from rest_framework.response import Response
from .models import Blog
from rest_framework import status
from django.http import Http404
# Create your views here.
class BlogView(APIView):
    def get(self,request,format=None):
        blogs=Blog.objects.all()
        serializers=BlogSerializers(blogs,many=True)
        return Response(serializers.data)
    def post(self,request,format=None):
        serializers=BlogSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class SingleBlogView(APIView):
    def get_single_blog(self,id):
        try:
            return Blog.objects.get(id=id)
        except Blog.DoesNotExist:
            raise Http404
    def get(self,request,id):
        blog=self.get_single_blog(id)
        serializers=BlogSerializers(blog)
        return Response(serializers.data)
    def put(self,request,id):
        blog=self.get_single_blog(id)
        serializers=BlogSerializers(blog,data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id):
        blog=self.get_single_blog(id)
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 


    
