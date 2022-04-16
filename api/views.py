from django.shortcuts import render
from .serializers import BlogSerializer
from .models import Blog
from rest_framework import viewsets

# Create your views here.
class BlogViewsets(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer