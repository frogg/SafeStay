from django.db import models

#TYPE_OF_CRIMES = (())


# Create your models here.

class Crime(models.Model):
    type = models.CharField(max_length=100);
    latitude = models.FloatField();
    longitude = models.FloatField();
