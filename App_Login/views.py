from django.shortcuts import render,HttpResponseRedirect,reverse
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponse 
from django.contrib.auth.decorators import login_required

# Create your views here.

def signUp(request):
    form = UserCreationForm()
    registered = False
    if request.method == 'POST':
        form = UserCreationForm(data = request.POST)
        if form.is_valid():
            form.save()
            registered = True
    dict = {'form':form,'registered':registered}
    return render(request,'App_Login/signup.html',context=dict)

def LogIn(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username = username,password = password)
            if user is not None:
                login(request,user)
                return render(request,'App_Login/user_home.html')
    return render(request,'App_Login/login.html',context={'form':form})

@login_required
def LogOut(request):
    logout(request)
    return HttpResponseRedirect(reverse('myblog:home'))


@login_required
def LogOut_X(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))
