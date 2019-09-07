#from django.shortcuts import render

# Create your views here.

    # posts/views.py
from django.views.generic import ListView, CreateView # new
from django.urls import reverse_lazy # new

from .forms import PostForm # new
from .models import Post

class HomePageView(ListView):
    model = Post
    template_name = 'home.html'

class CreatePostView(CreateView): # new
    model = Post
    form_class = PostForm
    template_name = 'post.html'
    success_url = reverse_lazy('home')