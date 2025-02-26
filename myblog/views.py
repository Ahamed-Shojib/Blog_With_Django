from django.http import HttpResponse 
from django.urls import reverse 
from django.shortcuts import HttpResponseRedirect,render


def home(request):
    #return HttpResponseRedirect(reverse('App_Blog:blog_list'))
    #return HttpResponse('Welcome to Home Page')
    return render(request,'base.html')
