from django.db import models
from bed.models import Bed

# Create your models here.
class Patient(models.Model):
    age = models.IntegerField()
    name = models.CharField()
    date_assigned = models.DateTimeField(auto_now_add=True)
    date_discharged = models.DateTimeField(null=True)

    def __str__(self):
        return "Patient: {}, age: {}".format(self.name, sefl.age)

class PatientBed(models.Model):
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    bed_id = models.ForeignKey(Bed, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

    def __str__(self):
        return "patient: {}, active: {}".format(self.patient_id, self.status)

class BaselineRecord(models.Model):
    blood_pressure = models.CharField()
    pulse_rate = models.CharField()
    temperature = models.CharField()
    respiratory_rate = models.CharField()
    oxygen_circulation = models.CharField()
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date_collected = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{0} patient with temperature of {1}".format(self.patient_id, self.temperature)