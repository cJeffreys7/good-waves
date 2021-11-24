from django.contrib import admin
from .models import RecommendationList, Podcast, Review

admin.site.register(RecommendationList)
admin.site.register(Podcast)
admin.site.register(Review)