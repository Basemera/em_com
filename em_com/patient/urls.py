from django.urls import path
from patient.views import PatientCreateView, PatientDetailView, BaselineRecordCreateView, PatientBedCreateView

urlpatterns = [
    path('create/', PatientCreateView.as_view(), name='create'),
    path('detail/<int:pk>/', PatientDetailView.as_view(), name='detail'),
    path('<int:pk>/baseline-record', BaselineRecordCreateView.as_view(), name='baseline-record'),
    path('<int:pk>/bed-assign', PatientBedCreateView.as_view(), name='assign-bed'),

]