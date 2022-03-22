from django import forms
from .models import Business, Post, Profile
from django.contrib.auth.models import User

class CreateUserForm(forms.ModelForm):
  class Meta:
    model = User
    fields = ('username', 'email',)

class ProfileForm(forms.ModelForm):
    class Meta:
      model = Profile
      fields = ['username', 'count',]

class BusinessForm(forms.ModelForm):
  class Meta:
    model = Business
    fields = '__all__'
    exclude = ['username', 'neighborhood',]

class PostForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ('title', 'story', )
    