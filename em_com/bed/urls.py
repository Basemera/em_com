from django.urls import path
from bed.views import BedCreateView, BedDetailView

urlpatterns = [
    path('create/', BedCreateView.as_view()),
    path('detail/<int:pk>/', BedDetailView.as_view()),
]