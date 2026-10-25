from django.shortcuts import render,redirect
from django.http import HttpResponse

def home_page_view(request):
    return HttpResponse('hello there') 