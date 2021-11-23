from django.urls import path

from main_app.models import RecommendationList, Podcast
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('about/', views.about, name='about'),
  path('accounts/signup/', views.signup, name='signup'),
  
  # recommendation list urls
  path('recs/', views.RecommendationListList.as_view(), name='recs_index'),
  path('recs/create/', views.RecommendationListCreate.as_view(), name='recs_create'),

  # podcast urls
  path('podcasts/create/', views.PodcastCreate.as_view(), name='podcasts_create')
]