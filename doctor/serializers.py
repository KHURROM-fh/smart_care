from rest_framework import serializers
from . import models  
class DesignationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Designation 
        fields = '__all__'  

class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Specialization 
        fields = '__all__'  

class AvailableTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AvailableTime 
        fields = '__all__' 

class DoctorSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)
    designation = serializers.StringRelatedField(many=True)
    spcialization = serializers.StringRelatedField(many=True)
    availableTime = serializers.StringRelatedField(many=True)
    class Meta:
        model = models.Doctor 
        fields = '__all__'  

class ReviewerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Reviewer 
        fields = '__all__'  
