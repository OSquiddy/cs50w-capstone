from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    fullname = serializers.CharField()
    class Meta:
        model = MyBaseUser
        fields = '__all__'
        
class DoctorSerializer(serializers.ModelSerializer):
    fullname = serializers.CharField()
    class Meta:
        model = Doctor
        fields = '__all__'
        
class PatientSerializer(serializers.ModelSerializer):
    sex = serializers.SerializerMethodField()
    fullname = serializers.CharField()

    def get_sex(self, obj):
        return obj.get_sex_display()
        
    class Meta:
        model = Patient
        exclude = ['password', 'last_login', 'is_superuser', 'is_staff', 'is_active', 'date_joined', 'groups', 'user_permissions']
        
class VisitSerializer(serializers.ModelSerializer):
    visit_number = serializers.IntegerField()
    class Meta:
        model = Visit
        fields = '__all__'
        
class ExaminationSerializer(serializers.ModelSerializer):
    visit_id = serializers.IntegerField()
    visit_number = serializers.ReadOnlyField(source='visit.visit_number')

    class Meta:
        model = Examination
        # fields = '__all__'
        exclude = ['visit']

class PastHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Examination
        fields = '__all__'

class GynecHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Examination
        fields = '__all__'
        
        