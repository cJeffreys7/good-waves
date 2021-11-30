from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

CATEGORIES = (
  ('H', 'History'),
  ('E', 'Educational'),
  ('R', 'Religious'),
  ('A', 'Audio Dramas'),
  ('S', 'Sports'),
  ('C', 'Comedy Casts'),
  ('O', 'Society and Culture'),
  ('F', 'Feminist'),
  ('L', 'Health'),
  ('D', 'Advice and Self-Help'),
  ('B', 'Business'),
  ('N', 'News and Politics'),
  ('P', 'Personal Journal'),
  ('I', 'Interview Cast'),
  ('V', 'Environment/Science'),
  ('T', 'Technology'),
  ('M', 'Crime'),
  ('K', 'Kids and Families'),
  ('W', 'Law'),
  ('U', 'Pop Culture'),
  ('Y', 'Philosophy'),
  ('G', 'Games and Hobbies')
)

class Podcast(models.Model):
  title = models.CharField(max_length=100)
  description = models.TextField(max_length=500)
  category = models.CharField(
    max_length=1,
    choices=CATEGORIES,
    default=CATEGORIES[0][0]
    )
  link = models.CharField(max_length=250)
  average_rating = models.FloatField(
    default=0
  )
  image = models.TextField(
    max_length=500,
    blank=True,
    null=True
    )
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.title

  def get_absolute_url(self):
      return reverse("podcasts_detail", kwargs={'podcast_id': self.id})

class Review(models.Model):
  rating = models.IntegerField()
  text = models.TextField(max_length=500)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  podcast = models.ForeignKey(Podcast, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.user.username}'s review of {self.podcast.title}"

  def get_absolute_url(self):
    return reverse("podcasts_detail", kwargs={'podcast_id': self.podcast.id})

class RecommendationList(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  podcasts = models.ManyToManyField(Podcast)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
      return reverse("recs_detail", kwargs={'pk': self.id})