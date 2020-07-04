from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post, Categoria

class PostList(ListView):
    queryset = Post.objects.filter(status=1).order_by('-data')
    template_name = 'index.html'

class PostDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'

