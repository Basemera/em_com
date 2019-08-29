from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from patient.models import Patient, PatientBed, BaselineRecord
from django.urls import reverse



class PatientCreateView(CreateView):
    model = Patient
    fields = ['age', 'name',]

class PatientDetailView(DetailView):
    model = (Patient, PatientBed, BaselineRecord)

    # def get_object(self):
    #     obj = super().get_object()
    #     patient_object.append(obj)
    #     return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class BaselineRecordCreateView(CreateView):
    model = BaselineRecord
    fields = [
        'blood_pressure', 
        'pulse_rate', 
        'temperature',
        'respiratory_rate', 
        'oxygen_circulation', 
        'patient_id', 
        ]
    context_template_name = "patient/patientbed_form.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        path = self.request.path
        ids = [int(s) for s in path.split('/') if s.isdigit()]
        patient_id = ids[0]
        patient = Patient.objects.get(pk=patient_id)
        self.patient = patient
        context['patient'] = patient
        return context
    
    

class PatientBedCreateView(CreateView):
    model = PatientBed
    fields  = ['bed_id', 'status',]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        path = self.request.path
        ids = [int(s) for s in path.split('/') if s.isdigit()]
        patient_id = ids[0]
        patient = Patient.objects.get(pk=patient_id)
        context['patient'] = patient
        return context
    
    def get_success_url(self):
        return reverse("patient:detail", kwarg={"pk": self.patient.pk})


