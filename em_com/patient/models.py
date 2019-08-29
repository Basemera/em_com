from django.db import models
from django.urls import reverse
from bed.models import Bed

# Create your models here.
class Patient(models.Model):
    age = models.IntegerField()
    name = models.CharField(max_length=50)
    date_assigned = models.DateTimeField(auto_now_add=True)
    date_discharged = models.DateTimeField(null=True)

    def __str__(self):
        return "Patient: {}, age: {}".format(self.name, self.age)
    
    def get_absolute_url(self):
        return f"/patient/{self.id}/baseline-record"

class PatientBed(models.Model):
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    bed_id = models.ForeignKey(Bed, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

    def __str__(self):
        return "patient: {}, active: {}".format(self.patient_id, self.status)

    def get_absolute_url(self):
        return reverse("patient:detail", kwargs={"pk":self.patient_id})

class BaselineRecord(models.Model):
    blood_pressure = models.CharField(max_length=50)
    pulse_rate = models.CharField(max_length=50)
    temperature = models.CharField(max_length=50)
    respiratory_rate = models.CharField(max_length=50)
    oxygen_circulation = models.CharField(max_length=50)
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date_collected = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{0} patient with temperature of {1}".format(self.patient_id, self.temperature)

    def get_absolute_url(self):
        return f"/patient/{self.patient_id}/bed-assign"

    