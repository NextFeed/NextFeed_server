from django.db import models

# Create your models here.
class Analyze(models.Model):
    first_feature = models.CharField(max_length = 30, help_text = 'Feature name')       # Feature name
    first_score = models.IntegerField(help_text = 'Feature score')                     # Feature score
    second_feature = models.CharField(max_length = 30, help_text = 'Feature name')
    second_score = models.IntegerField(help_text = 'Feature score')
    third_feature = models.CharField(max_length = 30, help_text = 'Feature name')
    third_score = models.IntegerField(help_text = 'Feature score')
    
class User(models.Model):
    username = models.CharField(max_length = 30, help_text = 'Account name')            # Instagram account name max
    usertype = models.CharField(max_length = 10, help_text = 'Account analyze type')            # Male, Female, ..?
    analyze_profile = models.ForeignKey(Analyze, on_delete = models.CASCADE, blank = True)
    
class Picture(models.Model):
    url = models.TextField(help_text = 'Image url')            # Image url
    analyze_picture = models.ForeignKey(Analyze, on_delete = models.CASCADE)
