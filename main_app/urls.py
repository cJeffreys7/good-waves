from django.urls import path

from main_app.forms import CustomAuthForm

from . import views

urlpatterns = [
  path('', views.Home.as_view(authentication_form=CustomAuthForm), name='home'),
  path('about/', views.about, name='about'),
  path('accounts/signup/', views.signup, name='signup'),
  
  # recommendation list urls
  path('recs/', views.RecommendationListList.as_view(), name='recs_index'),
  path('recs/create/', views.RecommendationListCreate.as_view(), name='recs_create'),
  path('recs/<int:rec_id>/', views.recs_detail, name='recs_detail'),
  path('recs/<int:rec_id>/assoc_podcast/<int:podcast_id>/', views.assoc_podcast, name='assoc_podcast'),
  path('recs/<int:rec_id>/unassoc_podcast/<int:podcast_id>/', views.unassoc_podcast, name='unassoc_podcast'),
  path('recs/<int:pk>/update/', views.RecommendationListUpdate.as_view(), name='recs_update'),
  path('recs/<int:pk>/delete/', views.RecommendationListDelete.as_view(), name='recs_delete'),

  # podcast urls
  path('podcasts/', views.PodcastList.as_view(), name='podcasts_index'),
  path('podcasts/create/', views.PodcastCreate.as_view(), name='podcasts_create'),
  path('podcasts/<int:podcast_id>/', views.podcasts_detail, name='podcasts_detail'),
  path('podcasts/<int:podcast_id>/add_review/', views.add_review, name='add_review'),
  path('podcasts/<int:pk>/update/', views.PodcastUpdate.as_view(), name='podcasts_update'),
  path('podcasts/<int:pk>/delete/', views.PodcastDelete.as_view(), name='podcasts_delete'),

  # review urls
  path('reviews/<int:pk>/update/', views.ReviewUpdate.as_view(), name='reviews_update'),
  path('reviews/<int:pk>/delete/', views.ReviewDelete.as_view(), name='reviews_delete')
]