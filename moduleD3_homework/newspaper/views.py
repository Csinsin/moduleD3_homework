from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *

class PostsList(ListView):
    model = Post
    template_name = 'posts.html'
    context_object_name = 'posts'
    queryset = Post.objects.order_by('-id')

class PostList(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'


def home(request):
    return render(request, 'home.html')
