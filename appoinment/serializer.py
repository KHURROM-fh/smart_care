from rest_framework import serializers
from . import models
class AppoinmentSerializer(serializers.ModelSerializer):
    time = serializers.StringRelatedField(many=False)
    patinet = serializers.StringRelatedField(many=False)
    doctor = serializers.StringRelatedField(many=False)

    class Meta:
        model = models.Appointment
        fields = '__all__'