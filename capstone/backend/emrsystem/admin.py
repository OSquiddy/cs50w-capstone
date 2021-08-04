from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

class VisitAdmin(admin.ModelAdmin):
    model = Visit
    list_display = ['id', 'patient', 'visit_number', 'date', 'time_from', 'time_till', 'assigned_doctor']
    readonly_fields = ('visit_number',)
    ordering = ['patient__first_name', 'visit_number']
    
    # def patient_name(self, obj):
    #     return obj.patient.first_name + ' ' + obj.patient.last_name
    # patient_name.admin_order_field = 'patient__first_name'

class CustomUserAdmin(admin.ModelAdmin):
    model = MyBaseUser
    readonly_fields = ['fullname']
    ordering = ['first_name']

class PatientAdmin(admin.ModelAdmin):
    model = Patient
    readonly_fields = ['fullname']
    list_display = ['first_name', 'last_name', 'username', 'email' ]
    ordering = ['first_name']


# Register your models here.
admin.site.register(MyBaseUser, CustomUserAdmin)
admin.site.register(Doctor)
admin.site.register(Patient, PatientAdmin)
admin.site.register(Visit, VisitAdmin)
admin.site.register(Examination)
admin.site.register(PastHistory)
admin.site.register(GynecHistory)
