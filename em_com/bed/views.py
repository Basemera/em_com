from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from bed.models import Bed

class BedCreateView(CreateView):
    model = Bed
    fields = ['bed_number', 'device_id']


class BedDetailView(DetailView):
    model = Bed

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
# Create your views here.
