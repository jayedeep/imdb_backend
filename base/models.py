from django.db import models

# Create your models here.
class Movies(models.Model):
    name=models.CharField(max_length=100)
    rating=models.FloatField()
    realise_date=models.DateField()
    duration=models.CharField(max_length=50)
    description=models.TextField()