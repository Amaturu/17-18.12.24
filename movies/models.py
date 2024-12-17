from django.db import models
from django.utils import timezone

class Movie(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField(max_length=150, blank=True, default='')
    release_date = models.DateField()
    rating = models.FloatField()

    class Meta:
        ordering = ['created']


