from django.shortcuts import render

# Create your views here.
from .models import Post
from django.views.generic import ListView

class PostListView(ListView):
    model = Post
    template_name = 'home.html'