from django.db import models

# Create your models here.
class Contact_us(models.Model):
    name= models.CharField(max_length=30)
    mobile_no= models.CharField(max_length=12)
    problem= models.TextField()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "ContactUs"

