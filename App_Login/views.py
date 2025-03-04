from django.shortcuts import render,HttpResponseRedirect,reverse
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordChangeForm
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponse 
from django.contrib.auth.decorators import login_required
from App_Login.forms import SignUpForm,UserChangeForm,EditProfileForm,profilePic

# Create your views here.

def signUp(request):
    form = SignUpForm()
    registered = False
    if request.method == 'POST':
        form = SignUpForm(data = request.POST)
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
                return render(request,'App_Blog/blog_list.html')
    return render(request,'App_Login/login.html',context={'form':form})

@login_required
def LogOut(request):
    logout(request)
    return HttpResponseRedirect(reverse('myblog:home'))


@login_required
def LogOut_X(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


#User Home
def user_home(request):
    return render(request,'App_Login/user_home.html')

#User Profile
def user_profile(request):
    return render(request,'App_Login/user_profile.html',context={})

#Change user profile
@login_required
def change_profile(request):
    current_user = request.user
    changed_profile = False
    form = EditProfileForm(instance=current_user)
    if request.method == 'POST':
        form = EditProfileForm(request.POST,instance=current_user)
        if form.is_valid():
            form.save()
            changed_profile = True
            form = EditProfileForm(instance=current_user)
    return render(request,'App_Login/change_profile.html',context={'form':form,'changed_profile':changed_profile})

#Change Password
@login_required
def change_password(request):
    current_user = request.user
    changed =  False
    form = PasswordChangeForm(current_user)
    if request.method == 'POST':
        form = PasswordChangeForm(current_user,data=request.POST)
        if form.is_valid():
            form.save()
            changed = True
            form = PasswordChangeForm(current_user)
    return render(request,'App_Login/change_password.html',context={'form':form,'changed':changed})


#Add Profile Pic
@login_required
def add_profile_pic(request):
    form = profilePic()
    if request.method == 'POST':
        form = profilePic(request.POST,request.FILES)
        if form.is_valid():
            user_obj = form.save(commit=False)
            user_obj.user = request.user
            user_obj.save()
            return HttpResponseRedirect(reverse('App_Login:user_profile'))
    return render(request,'App_Login/add_profile_pic.html',context={'form':form})

#Change Profile Pic
@login_required
def change_profile_pic(request):
    form = profilePic(instance=request.user.user_profile)
    if request.method == 'POST':
        form = profilePic(request.POST,request.FILES,instance=request.user.user_profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('App_Login:user_profile'))
    return render(request,'App_Login/add_profile_pic.html',context={'form':form})