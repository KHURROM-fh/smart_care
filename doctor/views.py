from django.shortcuts import render
from rest_framework import viewsets, pagination, filters
from . import models
from . import serializers  # Import only the necessary serializer
from rest_framework.permissions import IsAuthenticated, BasePermission, IsAuthenticatedOrReadOnly

# Create your views here.
class DesignationViewSet(viewsets.ModelViewSet):
    queryset = models.Designation.objects.all()
    serializer_class = serializers.DesignationSerializer 

class SpecializationViewSet(viewsets.ModelViewSet):
    queryset = models.Specialization.objects.all()
    serializer_class = serializers.SpecializationSerializer

class AvailableTimeForSpecificDoctor(filters.BaseFilterBackend):
    def filter_queryset(self, request, query_set, view):
        doctor_id = request.query_params.get("doctor_id")
        if doctor_id:
            return query_set.filter(doctor = doctor_id)
        return query_set

class AvailableTimeViewSet(viewsets.ModelViewSet):
    permission_classes= [IsAuthenticatedOrReadOnly]
    queryset = models.AvailableTime.objects.all()
    serializer_class = serializers.AvailableTimeSerializer
    filter_backends = [AvailableTimeForSpecificDoctor]

class DoctorPagination(pagination.PageNumberPagination):
    page_size= 1 #items per page
    page_size_query_param= page_size
    max_page_size = 100

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = models.Doctor.objects.all()
    serializer_class = serializers.DoctorSerializer
    filter_backends= [filters.SearchFilter]
    pagination_class= DoctorPagination 

class ReviewerViewSet(viewsets.ModelViewSet):
    queryset = models.Reviewer.objects.all()
    serializer_class = serializers.ReviewerSerializer 
