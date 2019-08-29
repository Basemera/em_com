from django.urls import path
from device.views import DeviceCreateView, DeviceDetailView

urlpatterns = [
    path('create/', DeviceCreateView.as_view()),
    path('detail/<int:pk>/', DeviceDetailView.as_view()),
]