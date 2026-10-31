from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import Post
from django.views.generic import ListView,DetailView, UpdateView, DeleteView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
class PostList(ListView):
    model = Post
    template_name = 'pages/home.html'
    
class PostDetail(DetailView):
    model = Post
    template_name = "pages/post_detail.html"
    
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'pages/post_new.html'
    fields = ['title','author','body']
    success_url = reverse_lazy('pages:home')
    
class PostUpdateView(LoginRequiredMixin,UpdateView):
    model = Post
    template_name = 'pages/post_edit.html'
    fields = ['title','body']

class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = Post
    template_name = 'pages/post_delete.html'
    success_url = reverse_lazy('pages:home')