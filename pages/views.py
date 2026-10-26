from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import Post
from django.views.generic import ListView
# def post_list(request):
#     posts = Post.objects.all()
#     context = {'posts': posts}
#     return render(request, 'pages/post_list.html',context)

class PostList(ListView):
    model = Post
    template_name = 'pages/post_list.html'