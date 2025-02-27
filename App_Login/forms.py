from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="Email Address",required=True)
    class Meta:
        model = User
        fields = ('username','email','password1','password2')

class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username','email','first_name','last_name','password')