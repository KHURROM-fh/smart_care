from django.db import models
from doctor.models import Doctor, AvailableTime
from patient.models import Patinet  # Fixed typo from 'Patinet' to 'Patient'

# Appointment choices
APPOINTMENT_TYPE = [
    ('Pending', 'Pending'),
    ('Running', 'Running'),
    ('Completed', 'Completed'),
]

APPOINTMENT_STATUS = [
    ('Offline', 'Offline'),
    ('Online', 'Online'),
]

class Appointment(models.Model):  # Fixed spelling from 'Appoinment'
    patinet = models.ForeignKey(Patinet, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_type = models.CharField(max_length=10, choices=APPOINTMENT_TYPE, default="Pending")  # Fixed typo
    appointment_status = models.CharField(max_length=10, choices=APPOINTMENT_STATUS)  # Fixed typo
    symptom = models.TextField()
    time = models.ForeignKey(AvailableTime, on_delete=models.CASCADE)
    cancel = models.BooleanField(default=False)

    def __str__(self):
        return f"Appointment({self.patinet} - {self.doctor} at {self.time.time}, Status: {self.appointment_status})"
