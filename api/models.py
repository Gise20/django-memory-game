from django.db import models

# Create your models here.
class ConfigNumberCards(models.Model):
    Easy = models.PositiveSmallIntegerField() 
    Medium = models.PositiveSmallIntegerField() 
    Hard  = models.PositiveSmallIntegerField() 

class ConfigTimeBonus(models.Model):
    Easy = models.PositiveSmallIntegerField() 
    Medium = models.PositiveSmallIntegerField() 
    Hard = models.PositiveSmallIntegerField() 

class SaveHighScores(models.Model):
    Difficulty = models.CharField(max_length=6)
    PlayerName = models.CharField(max_length=30)
    Score = models.PositiveIntegerField()
    Date = models.DateField(auto_now_add=True)