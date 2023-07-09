from django.db import models

class City(models.Model):
    name = models.CharField(max_length=100)
    temperature = models.FloatField()
    humidity = models.IntegerField()
    weather_status = models.CharField(max_length=100)

    def __str__(self):
        return self.name