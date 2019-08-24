from django.db import models

class Device(models.Model):
    temperature = models.IntegerField()
    timestamp = models.DateTimeField()

    def __str__(self):
        return f"{0} degrees Celcius at {1}".format(self.temperature, self.timestamp)
