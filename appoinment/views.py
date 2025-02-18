from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializer

class AppoinmentViewSet(viewsets.ModelViewSet):
    queryset = models.Appointment.objects.all()
    serializer_class = serializer.AppoinmentSerializer

    #custom query kortechi
    def get_queryset(self):
        queryset = super().get_queryset()
        patient_id = self.request.query_params.get('patient_id')
        
        if patient_id:
            queryset = queryset.filter(patinet_id=patient_id)  # Use 'patinet_id' instead of 'patient_id'
    
        return queryset

