from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import Post
from django.views.generic import ListView,DetailView
# def post_list(request):
#     posts = Post.objects.all()
#     context = {'posts': posts}
#     return render(request, 'pages/post_list.html',context)

class PostList(ListView):
    model = Post
    template_name = 'pages/home.html'
    
class PostDetail(DetailView):
    model = Post
    template_name = "pages/post_detail.html"