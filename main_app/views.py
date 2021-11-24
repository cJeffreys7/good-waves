from django.shortcuts import render, redirect

from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

from main_app.models import RecommendationList, Podcast, Review
from .forms import CustomRegForm, ReviewForm

def about(request):
  return render(request, 'about.html')

class Home(LoginView):
  template_name = 'home.html'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = CustomRegForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('home')
    else:
      error_message = 'Invalid sign up - try again'
  form = CustomRegForm()
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

def podcasts_detail(request, podcast_id):
  podcast = Podcast.objects.get(id=podcast_id)
  review_form = ReviewForm()
  return render(request, 'podcasts/detail.html', {'podcast': podcast, 'review_form': review_form})

def add_review(request, podcast_id):
  form = ReviewForm(request.POST)
  if form.is_valid():
    new_review = form.save(commit=False)
    new_review.podcast_id = podcast_id
    new_review.user = request.user
    new_review.save()
  return redirect('podcasts_detail', podcast_id=podcast_id)

class PodcastUpdate(UpdateView):
  model = Podcast
  fields = ['title', 'description', 'category', 'link']

class PodcastDelete(DeleteView):
  model = Podcast
  success_url = '/podcasts/'

class ReviewUpdate(UpdateView):
  model = Review
  fields = ['rating', 'text']

class ReviewDelete(DeleteView):
  model = Review
  success_url = '/podcasts/'