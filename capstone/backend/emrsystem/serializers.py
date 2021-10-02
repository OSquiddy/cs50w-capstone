from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    sex = serializers.SerializerMethodField()
    fullname = serializers.CharField()

    def get_sex(self, obj):
        return obj.get_sex_display()

    class Meta:
        model = MyBaseUser
        exclude = ['password', 'last_login', 'is_superuser', 'is_staff', 'is_active', 'date_joined', 'groups', 'user_permissions']
        
class DoctorSerializer(serializers.ModelSerializer):
    sex = serializers.SerializerMethodField()
    fullname = serializers.CharField()

    def get_sex(self, obj):
        return obj.get_sex_display()

    class Meta:
        model = Doctor
        exclude = ['password', 'last_login', 'is_superuser', 'is_staff', 'is_active', 'date_joined', 'groups', 'user_permissions']
        
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
        model = PastHistory
        fields = '__all__'

class GynecHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GynecHistory
        fields = '__all__'
        
        