from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def blog_list(request):
    return HttpResponse('Welcome to Blog List Page')