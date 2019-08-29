from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from device.models import Device

class DeviceCreateView(CreateView):
    model = Device
    fields = ['temperature',]


class DeviceDetailView(DetailView):
    model = Device

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context