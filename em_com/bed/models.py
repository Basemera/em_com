from django.db import models
from device.models import Device

# Create your models here.

class Bed(models.Model):
    bed_number = models.IntegerField()
    device_id = models.ForeignKey(Device, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{0} with device {1}".format(self.bed_number, self.device_id)

    def get_absolute_url(self):
        return f"/bed/detail/{self.id}/"