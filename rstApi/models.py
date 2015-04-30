from django.db import models

class VideoData(models.Model):
	name = models.CharField(max_length=100)
	popularity = models.FloatField(default=0.0)
	director = models.CharField(max_length=100)
	genere = models.CharField(max_length=100)
	imdb_score = models.FloatField(default=0.0)
	owner = models.ForeignKey('auth.User', related_name='videoOwner')

