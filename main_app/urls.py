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
  path('recs/<int:pk>/', views.RecommendationListDetail.as_view(), name='recs_detail'),
  path('recs/<int:pk>/update/', views.RecommendationListUpdate.as_view(), name='recs_update'),
  path('recs/<int:pk>/delete/', views.RecommendationListDelete.as_view(), name='recs_delete'),

  # podcast urls
  path('podcasts/', views.PodcastList.as_view(), name='podcasts_index'),
  path('podcasts/create/', views.PodcastCreate.as_view(), name='podcasts_create'),
  path('podcasts/<int:podcast_id>/', views.podcasts_detail, name='podcasts_detail'),
  path('podcasts/<int:podcast_id>/add_review/', views.add_review, name='add_review'),
  path('podcasts/<int:pk>/update/', views.PodcastUpdate.as_view(), name='podcasts_update'),
  path('podcasts/<int:pk>/delete/', views.PodcastDelete.as_view(), name='podcasts_delete')
]