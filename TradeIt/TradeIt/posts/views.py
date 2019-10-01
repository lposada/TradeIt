from django.shortcuts import render, get_object_or_404
from .models import Post, Category
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .forms import PostForm
from django.urls import reverse, reverse_lazy
# Create your views here.

class ListPost(ListView):
    model = Post

class ListCategory(ListView):
    model = Category

class DetailPost(DetailView):
    model = Post

class CrearPost(CreateView):
    form_class = PostForm
    template_name = "posts/post_form.html"
    success_url = reverse_lazy('posts:posts')