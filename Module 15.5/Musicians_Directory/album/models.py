from django.db import models
from musician.models import Musician
from django import forms
RATINGS = [('1','1' ),('2','2'),('3','3'),('4','4'),('5','5')]
# Create your models here.
class Album(models.Model):
        album_name = models.CharField(max_length=25)
        musician = models.ForeignKey(Musician, on_delete = models.CASCADE)
        album_release_date = models.DateField()
        rating = models.CharField(max_length=1,choices = RATINGS)

        def __str__(self):
                return f"{self.album_name} by {self.musician.first_name}"