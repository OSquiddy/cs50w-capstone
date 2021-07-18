from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyBaseUser
        fields = '__all__'
        
class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'
        
class PatientSerializer(serializers.ModelSerializer):
    sex = serializers.SerializerMethodField()

    def get_sex(self, obj):
        return obj.get_sex_display()
        
    class Meta:
        model = Patient
        exclude = ['password', 'last_login', 'is_superuser', 'is_staff', 'is_active', 'date_joined', 'groups', 'user_permissions']
        
class VisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = '__all__'
        
class ExaminationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Examination
        fields = '__all__'

class PastHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Examination
        fields = '__all__'

class GynecHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Examination
        fields = '__all__'
        
        