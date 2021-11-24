from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .models import Review

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