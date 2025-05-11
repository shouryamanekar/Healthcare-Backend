from django.urls import path
from .views import (
    PatientListCreateView, PatientDetailView,
    MappingCreateView, MappingListView,
    PatientDoctorListView, MappingDeleteView
)

urlpatterns = [
    path('', PatientListCreateView.as_view(), name='patient-list-create'),
    path('<int:pk>/', PatientDetailView.as_view(), name='patient-detail'),
    path('mappings/', MappingListView.as_view(), name='mapping-list'),
    path('mappings/create/', MappingCreateView.as_view(), name='mapping-create'),
    path('mappings/<int:patient_id>/', PatientDoctorListView.as_view(), name='patient-doctors'),
    path('mappings/delete/<int:pk>/', MappingDeleteView.as_view(), name='mapping-delete'),
]
