from rest_framework import serializers
from .models import *


def profile_pic_url(obj, context):
    if not obj.profilePic:
        return ''

    request = context.get('request')
    url = obj.profilePic.url
    if request and url.startswith('/'):
        return request.build_absolute_uri(url)
    return url


class UserSerializer(serializers.ModelSerializer):
    sex_full = serializers.SerializerMethodField()
    sex = serializers.CharField()
    fullname = serializers.SerializerMethodField()
    profilePic = serializers.SerializerMethodField()

    def get_sex_full(self, obj):
        return obj.get_sex_display()

    def get_fullname(self, obj):
        return obj.fullname()

    def get_profilePic(self, obj):
        return profile_pic_url(obj, self.context)

    class Meta:
        model = MyBaseUser
        exclude = ['password', 'last_login', 'is_superuser', 'is_staff', 'is_active', 'date_joined', 'groups', 'user_permissions']


class DoctorSerializer(serializers.ModelSerializer):
    sex_full = serializers.SerializerMethodField()
    sex = serializers.CharField()
    fullname = serializers.SerializerMethodField()
    profilePic = serializers.SerializerMethodField()

    def get_sex_full(self, obj):
        return obj.get_sex_display()

    def get_fullname(self, obj):
        return obj.fullname()

    def get_profilePic(self, obj):
        return profile_pic_url(obj, self.context)

    class Meta:
        model = Doctor
        exclude = ['password', 'last_login', 'is_superuser', 'is_staff', 'is_active', 'date_joined', 'groups', 'user_permissions']


class PatientSerializer(serializers.ModelSerializer):
    sex_full = serializers.SerializerMethodField()
    sex = serializers.CharField()
    fullname = serializers.SerializerMethodField()
    profilePic = serializers.SerializerMethodField()

    def get_sex_full(self, obj):
        return obj.get_sex_display()

    def get_fullname(self, obj):
        return obj.fullname()

    def get_profilePic(self, obj):
        return profile_pic_url(obj, self.context)

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
