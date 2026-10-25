from django.shortcuts import render,redirect
from django.http import HttpResponse

def home_page_view(request):
    return HttpResponse('hello there') 

def about_page_view(request):
    context = {'name': 'Lazizbek'}
    return render(request, 'pages/about.html', context)
