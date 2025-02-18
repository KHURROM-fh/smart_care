from django.contrib import admin
from .models import Appointment  
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.shortcuts import redirect
from django.contrib.auth.models import User 

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("id", "patinet", "doctor", "time", "appointment_status", "cancel")  # Fixed typo
    list_filter = ("appointment_status", "cancel")  # Fixed typo
    search_fields = ("patinet__name", "doctor__name")
    ordering = ("time",)

    def save_model(self, request, obj, form, change):
        obj.save()
        if obj.appointment_status== "Running" and obj.appointment_type == "Online":
            email_subject= "Your Online Appointment is Running"
            email_body= render_to_string('admin_email.html', {'user' : obj.patient.user, 'doctor' : obj.doctor})
            email= EmailMultiAlternatives(email_subject, '', to=[obj.patient.user.email])
            email.attach_alternative(email_body, "text/html")
            email.send()


