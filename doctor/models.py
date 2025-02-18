from django.db import models
from django.contrib.auth.models import User
from patient.models import Patinet
# Create your models here.
class Designation(models.Model):
    name= models.CharField(max_length=30)
    slug= models.SlugField(max_length= 32)

    def __str__(self):
        return self.name

class Specialization(models.Model):
    name= models.CharField(max_length=30)
    slug= models.SlugField(max_length=30)

    def __str__(self):
        return self.name

class AvailableTime(models.Model):
    time = models.TimeField()
    def __str__(self):
        return str(self.time)

class Doctor(models.Model):
    user= models.OneToOneField(User, on_delete= models.CASCADE)
    img= models.ImageField(upload_to="doctor/images/")
    designation= models.ManyToManyField(Designation)
    spcialization= models.ManyToManyField(Specialization)
    availableTime= models.ManyToManyField(AvailableTime)
    fees= models.IntegerField()
    meet= models.TextField()

    def __str__(self):
        return f"Dr. {self.user.first_name} {self.user.last_name}"
    
STAR_RATING = [
    ('⭐', '⭐'),
    ('⭐⭐', '⭐⭐'),
    ('⭐⭐⭐', '⭐⭐⭐'),
    ('⭐⭐⭐⭐', '⭐⭐⭐⭐'),
    ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐'),
]

class Reviewer(models.Model):
    reviewer = models.ForeignKey(Patinet, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    body = models.TextField()
    on_created = models.DateTimeField(auto_now_add=True)
    rating = models.CharField(max_length=10, choices=STAR_RATING) 
    
    def __str__(self):
        return f"{self.reviewer} rated {self.doctor}: {self.rating}"
