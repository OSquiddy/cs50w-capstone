from rest_framework import serializers
from .models import User, Doctor, Patient

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        
class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        
class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        
        