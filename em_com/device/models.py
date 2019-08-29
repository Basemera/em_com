from django.db import models
from django.urls import resolvers

class Device(models.Model):
    temperature = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{0} degrees Celcius at {1}".format(self.temperature, self.timestamp)

    def get_absolute_url(self):
        return f"/device/detail/{self.id}/"