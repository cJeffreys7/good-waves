from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from .models import Podcast, Review

class PodcastForm(ModelForm):

  class Meta:
    model = Podcast
    fields = ['title', 'description', 'category', 'link']

    widgets = {
      'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Podcast Title'})
    }

class ReviewForm(ModelForm):

  class Meta:
    model = Review
    fields = ['rating', 'text']

class CustomAuthForm(AuthenticationForm):
  class Meta:
    model = User
    fields = ['username','password']

  def __init__(self, *args, **kwargs):
    super(CustomAuthForm, self).__init__(*args, **kwargs)
    self.fields['username'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})
    self.fields['username'].label = False
    self.fields['password'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Password'}) 
    self.fields['password'].label = False

class CustomRegForm(UserCreationForm):
  class Meta:
    model = User
    fields = ['first_name', 'last_name', 'username','password1', 'password2']

    widgets = {
      'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
      'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
      'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'})
    }

  def __init__(self, *args, **kwargs):
    super(CustomRegForm, self).__init__(*args, **kwargs)
    self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
    self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'})