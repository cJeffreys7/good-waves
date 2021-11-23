from django.shortcuts import render, redirect

from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

from main_app.models import RecommendationList, Podcast

def about(request):
  return render(request, 'about.html')

class Home(LoginView):
  template_name = 'home.html'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in
      login(request, user)
      return redirect('home')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)

class RecommendationListList(ListView):
  model = RecommendationList

class RecommendationListCreate(CreateView):
  model = RecommendationList
  fields = ['name', 'description']
  success_url = '/recs/'

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class RecommendationListDetail(DetailView):
  model = RecommendationList

class RecommendationListUpdate(UpdateView):
  model = RecommendationList
  fields = ['name', 'description']
  
class RecommendationListDelete(DeleteView):
  model = RecommendationList
  success_url = '/recs/'

class PodcastList(ListView):
  model = Podcast

class PodcastCreate(CreateView):
  model = Podcast
  fields = ['title', 'description', 'category', 'link']
  success_url = '/about/'

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class PodcastDetail(DetailView):
  model = Podcast