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

class ExaminationAdmin(admin.ModelAdmin):
    model = Examination
    list_display = ['id', 'visit']
    ordering = ['visit__patient__first_name', 'visit__visit_number']
    fieldsets = ((None, { 'fields': ('visit', 'complaints', 'blood_pressure', 'SpO2', 'temperature', 'pulse_rate', 'respiratory', 'cardiovascular', 'cereberovascular', 'per_abdominal', 'local_examination')}),('General', { 'fields': (('pallor', 'clubbing', 'lymphadenopathy'), ('icterus', 'koilonychia'), 'others')}),('Diagnosis', { 'fields': ('diagnosis',)}) )

class CustomUserAdmin(admin.ModelAdmin):
    model = MyBaseUser
    readonly_fields = ['fullname']
    list_display = ['id', 'first_name', 'last_name', 'username', 'email' ]
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
admin.site.register(Examination, ExaminationAdmin)
admin.site.register(PastHistory)
admin.site.register(GynecHistory)
